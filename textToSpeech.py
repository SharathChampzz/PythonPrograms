import os
import playsound
from gtts import gTTS

i = 0


def speak(text):
    global i
    filename = 'voice' + str(i) + '.mp3'
    i += 1
    audio = gTTS(text=text, lang='en')
    audio.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


while 1:
    x = input('Type Here : ')
    speak(x)