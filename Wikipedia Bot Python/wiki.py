import wikipedia
import os
import playsound
from gtts import gTTS
import sys
import speech_recognition as sr
r = sr.Recognizer()
from time import sleep
i = 0


def speak(text):
    global i
    filename = 'voice' + str(i) + '.mp3'
    i += 1
    audio = gTTS(text=text, lang='en')
    audio.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


x = ""
def remov(y):
        global x
        x = y
        try:
                ind1 = x.index('(')
                ind2 = x.index(')')
                try:
                        check = x.index('(',ind1+1 , ind2)
                        if check != 0 :
                                repl = x[check-1:ind2+1]
                                x = x.replace(repl , "")
                                #print(x)
                                remov(x)
                except ValueError:
                        re = x[ind1-1:ind2+1]
                        x = x.replace(re , "")
                        remov(x)
                
        except ValueError:
                pass


while True:
	try:
		#condition = input('Do you want to ask Something ? y/n : ').lower() ##
		if True: ## condition == 'y'
			playsound.playsound("intro.mp3")
			#print('How can i help you sir!')
			sleep(1)
			with sr.Microphone() as source:
				audio = r.listen(source)
				question = r.recognize_google(audio)
				print(question)
				print('Searching for... {}'.format(question))
				playsound.playsound("gotquestion.mp3")
				sleep(4)
				query = wikipedia.page(question)
				print(query.summary)
				x = query.summary.split('.')[0]
				#print(x)
				remov(x)
				#print(x)
				speak(x)
				playsound.playsound("tq.mp3")
				break ##
				#m = input('Click "m" key to know more!  else any other key!!  : ').lower()
				#if m == 'm':
				#s	print(query.summary)				
		else:
			break

	except Exception as e:
		#speak(e)
		print(e)
		playsound.playsound("notfound.mp3")
		sleep(2)
		break