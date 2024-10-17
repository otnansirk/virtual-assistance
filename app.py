import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

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

            print(voice_to_text)
            reading(voice_to_text)


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