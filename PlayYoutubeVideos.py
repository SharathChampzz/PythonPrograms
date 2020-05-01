import pywhatkit as kit
import os
import playsound
from gtts import gTTS
import sys
import speech_recognition as sr
r = sr.Recognizer()

i = 0


def speak(text):
    global i
    filename = 'voice' + str(i) + '.mp3'
    i += 1
    audio = gTTS(text=text, lang='en')
    audio.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


speak("Sir! Which Video song you want me to play?")
with sr.Microphone() as source:
        print("Listening...!!")
        audio = r.listen(source)

        try:
            songname = r.recognize_google(audio)
        except Exception as e:
            print(e)
    
##songname = input('What song do you want me to play?  : ')
try:
        kit.playonyt(songname)
        speak("Playing.. " + songname)
        print("Playing..   " + songname)
except Exception as e:
        speak("Sir Some error Occured... Sorry!")
