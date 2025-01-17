import speech_recognition as sr
from gtts import gTTS
import playsound

def text_2_speech(text):
    txt2speech = gTTS(text, lang="id")
    txt2speech.save("my-voice.mp3")
    playsound.playsound("my-voice.mp3")

def listen_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            print("Listening...")
            recognizer.pause_threshold = 0.7
            audio = recognizer.listen(source)
            text  = recognizer.recognize_google(audio, language="id-ID")
            if "hai tami" in text.lower():
                text_2_speech(text="Oke bos")
            else:
                text_2_speech(text=text.lower())

            
            print(text)
        except sr.UnknownValueError:
            print("Suara tidak jelas.")

def run():
    while(True):
        listen_voice()

run()