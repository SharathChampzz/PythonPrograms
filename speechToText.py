import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    while 1:
        print("Listening...!!")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
            if text == 'quit':
                break

        except Exception as e:
            print(e)
print('Bye Bye User..!!')
