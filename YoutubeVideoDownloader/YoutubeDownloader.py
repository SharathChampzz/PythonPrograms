import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import threading

master = tk.Tk()
dest = StringVar()

def running(s):
	subprocess.call( s , shell=True , cwd = dest.get())

def download_video():
	if dest.get() is '':  # Check whether User chosen Destination or not
		destination_label.configure(text='Please Select Destination!')
	else:   
		link = e1.get()
		if link == '':  # Checking whether User gave Link or not
			destination_label.configure(text='Paste Link!')
			return
		elif 'playlist' in link:   # Particular actions for Playlist
			if var.get() == 0:
				destination_label.configure(text='Playlist Found.. Please Select Actions Below')
			elif var.get() == 1:
				destination_label.configure(text='Downloading.. All Actions will be Stopped!')
				cmd = 'youtube-dl -i ' + link
				th = threading.Thread(target=running, args=(cmd,))
				th.start()
			elif var.get() == 2:
				destination_label.configure(text='Downloading.. Range of Videos All Actions will be Stopped!')
				r = ran.get().split('-')
				cmd = 'youtube-dl --playlist-start ' + str(r[0]) + ' --playlist-end ' + str(r[1]) + ' ' + link
				th = threading.Thread(target=running, args=(cmd,))
				th.start()
			else:
				destination_label.configure(text='Some Error!')
		else:     # Single Video Link Found and it will download
			cmd = 'youtube-dl -i ' + link.split('&')[0]
			th = threading.Thread(target=running, args=(cmd,))
			th.start()

def destination():  # Opening File Dialog to select Destination Folder
	global dest
	act = filedialog.askdirectory()
	dest.set(act)
	print(f'Selectedzz : {dest.get()}')
	destination_label.configure(text=dest.get())

def sel():   # Radio Button Function On Choosing
	if var.get() == 2:
   		selection = "Give Range eg: 5-9"
   		label.config(text = selection)

	if var.get() == 1:
   		selection = "You selected to Download Full playlist"
   		label.config(text = selection)	
master.title("Youtube Downloader")

tk.Label(master,text="Enter URL Here").grid(row=0)


e1 = tk.Entry(master , textvariable='Ctrl + V')
e1.grid(row=0, column=1)

tk.Button(master, text='Download Video', command=download_video).grid(row=3, column=1,sticky=tk.W,pady=4)
tk.Button(master, text='Select Destination', command=destination).grid(row=0, column=2,sticky=tk.W,pady=4)
destination_label = ttk.Label(master, text= "WELCOME BACK DUDE!" , foreground = 'red' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold'))
destination_label.grid(column = 6, row = 0 , sticky=tk.W,pady=4)


var = IntVar()
R1 = Radiobutton(master, text="Download Full Playlist", variable=var, value=1,
                  command=sel).grid(row= 4 , column = 0)

R2 = Radiobutton(master, text="Range of Videos", variable=var, value=2,
                  command=sel).grid(row= 5 , column = 0)
ran = tk.Entry(master , width=10)

ran.grid(row=5, column=1)


label = Label(master)
label.grid(row= 7 , column = 0)
tk.mainloop()
