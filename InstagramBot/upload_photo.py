from instabot import Bot
from tkinter.filedialog import askopenfilename
from tkinter import *
import threading


username = ''  # Enter User name and Password 
password = ''

bot = Bot() 
bot.login(username = username, password = password)


file_path = ''
caption = ''

window = Tk()

def upload():
	global file_path, caption
	path.configure(text='Uploading Please Wait..!!', foreground = 'blue')
	bot.upload_photo(file_path , caption = caption)
	try:
		import os
		os.rename(file_path + '.REMOVE_ME', file_path)
		path.configure(text='Done!', foreground = 'green')
	except:
		path.configure(text='Failed to Upload Check log!', foreground = 'red')


def selectimg():
	global file_path
	file_path = askopenfilename(filetypes = [("Image" , ("*.png", "*.jpeg", "*.jpg" ))])
	path.configure(text=file_path, foreground = 'green')

def complete():
	global file_path, caption
	caption = l2.get("1.0","end-1c")
	threading.Thread(target=upload).start()
	

window.geometry('300x275')

Button(window,text = 'Select Image', command = selectimg).pack()

path = Label(window, text = 'No File Selected!', foreground= 'red')
path.pack()

Label(window, text = 'Enter Caption Here : ').pack()

l2 = Text(window, width= 30, height= 10)
l2.pack()

Button(window, text = 'Done', command = complete).pack()

window.mainloop()
