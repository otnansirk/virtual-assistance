import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from openai import OpenAI
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

def genai_wrapper(promt):
    genai.configure(api_key=os.environ["GPT_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(promt)
    return response.text

def reading(text):
    tts = gTTS(text=text, lang='id')
    tts.save('speech.mp3')
    playsound('/Users/otnansirk/OPEN_SOURCE/VA/speech.mp3')

def voice_job():
    recog = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        recog.pause_threshold = 0.7
        voice = recog.listen(source)

        try:
            print("Recognizing")
            voice_to_text = recog.recognize_google(voice, language="id-ID").lower()
            if(voice_to_text == 'terima kasih'):
                reading("Sama sama, senang bisa membantu")
                exit()

            voice_res = genai_wrapper(voice_to_text)

            print('Processing...')
            reading(voice_res)


        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def run():
    while(True):
        service = voice_job()

run()