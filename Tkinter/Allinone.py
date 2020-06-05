# pip install docx2pdf pillow PyPDF2
# Code is not optimised one , will do that in future
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from docx2pdf import convert 
from PIL import Image
from os import listdir
import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
import comtypes.client
from time import sleep
import subprocess

def action(variable):
	global sourcevar , destvar , mynumber , perform
	perform = mynumber.get()
	if perform == "Docx to PDF":
		if variable == 2:
			act = "PDF will be saved in the Same directory!"
		else:
			act = filedialog.askopenfilename(filetypes = [("Docx File" , "*.docx")])
	elif perform == "Images to PDF" or perform == "Merge PDFs" or perform == "PPT to PDF":
		act = filedialog.askdirectory()
	elif perform == "":
		act = "Please Select Action Above Before Trying!!"
		resultlab.configure(text= f'Please Select Action Above Before Trying!!' , foreground = 'red')
	else:
		print('Error Occured..!!!')

	if variable == 1:
		sourcevar = act
		source.configure(text= sourcevar)
		print(f'Source : {sourcevar}')
	elif variable == 2:
		destvar = act
		dest.configure(text=destvar)
		print(f'Destination : {destvar}')
	else:
		resultlab.configure(text = 'Unhandled Action!')


def browse_source():
	action(1)

def browse_dest():
    action(2)


def chosingNumbers():
    label.configure(text = "You Have Choosen " + mynumber.get())

def result():
	global perform , mynumber
	perform = mynumber.get()
	print('Process Running...')
	try:
		if perform == "Docx to PDF":
			docx2pdf()
		elif perform == "Images to PDF":
			im2pdf()
		elif perform == "Merge PDFs":
			mergepdf()
		elif perform == "PPT to PDF":
			ppt2pdf()
		elif perform == "":
			print("Please Select Action Above Before Trying!!")
			resultlab.configure(text= f'Saved! PDFs at {destvar}')
		else:
			print('Error Occured..!!!')
	except Exception as e:
		resultlab.configure(text = e)

def docx2pdf():
	resultlab.configure(text= 'Please Wait... Converting Docx to PDF')
	print('Converting Docx to PDF')
	sleep(1)
	destvar = sourcevar.replace('.docx','.pdf')
	convert(sourcevar , destvar)
	print('\nConverted Successfully!!\n')
	print(f'File Sucessfully Saved as {destvar}')
	resultlab.configure(text= f'File Sucessfully Saved as {destvar}')

def im2pdf():
	print('Converting Images to PDF')
	imagelist = []
	for image in listdir(sourcevar):
		imgPath = sourcevar + '/' + image
		if imgPath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
			print(f'Entered Inside with file {imgPath}')
			img = Image.open(imgPath).convert('RGB')
			imagelist.append(img)
		else:
			print(f'Extension Not Found in {imgPath}')
			continue
	im1 = imagelist[0]
	imagelist.pop(0)
	im1.save(destvar + '/ImageToPD.pdf' , save_all= True , append_images=imagelist)
	print(f'Saved! PDF at {destvar}')
	resultlab.configure(text= f'Saved! PDF at {destvar}')

def mergepdf():
	print('Merging PDFs')
	mergedObject = PdfFileMerger()
	for pdf in os.listdir(sourcevar):
		if pdf.lower().endswith(('.pdf')):
		 	PdfName = sourcevar + '/' + pdf
		 	mergedObject.append(PdfFileReader(PdfName, 'rb'))	 
	
	OutputName = destvar + '/MergedPDF.pdf'
	mergedObject.write(OutputName)
	print(f'Saved! Merged PDF at {OutputName}')
	resultlab.configure(text= f'Saved! PDF at {OutputName}' , foreground = 'red')

def ppt2pdf():
	print('Converting PPTs to PDFs')
	resultlab.configure(text= 'Converting PPTs to PDFs')
	input_folder_path = os.path.abspath(sourcevar.replace('/','\\'))
	output_folder_path = os.path.abspath(destvar.replace('/','\\'))

	input_file_paths = os.listdir(input_folder_path)
	print(f'Total Files Found {len(input_file_paths)}')

	for input_file_name in input_file_paths:
	    if not input_file_name.lower().endswith((".ppt", ".pptx")):
	        continue
	    input_file_path = os.path.join(input_folder_path, input_file_name)
	    print(f'Processing... {input_file_path}')
	    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
	    powerpoint.Visible = 1
	    slides = powerpoint.Presentations.Open(input_file_path)
	    file_name = os.path.splitext(input_file_name)[0]
	    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
	    slides.SaveAs(output_file_path, 32)
	    slides.Close()
	    resultlab.configure(text= f'Saved! PDFs at {destvar}')


window = tk.Tk()
window.minsize(400, 200)
window.title("All In One")


label = ttk.Label(window, text = "Choose Action Here -->>"  , foreground = 'black' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold'))
label.grid(column = 1, row = 1)

mynumber = tk.StringVar()
sourcevar = StringVar()
destvar = StringVar()
perform = StringVar()

combobox = ttk.Combobox(window, width = 15 , textvariable = mynumber)
combobox['values'] = ("Docx to PDF","Images to PDF","Merge PDFs","PPT to PDF")
combobox.grid(column = 2, row = 1)


source = ttk.Label(window, text= "Source location" , foreground = 'blue' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold'))
source.grid(column = 1, row = 4)
browse1 = ttk.Button(window, text = "Browse Source!", command = browse_source )  #1 for source location
browse1.grid(column = 2 , row = 4)

dest = ttk.Label(window, text= "Destination location" , foreground = 'blue' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold'))
dest.grid(column = 1, row = 6)
browse2 = ttk.Button(window, text = "Browse Destination", command = browse_dest ) #2 for destination location
browse2.grid(column = 2 , row = 6  , ipady = 4 , ipadx = 5)

button = ttk.Button(window, text = "Run", command = result)
button.grid(column = 2, row = 8)

resultlab = ttk.Label(window, text= "Actions Will be Displayed Here" , foreground = 'red' , background = 'white' ,font = ('Times New Roman' , 16 , 'bold') )
resultlab.grid(column = 1, row = 10 , ipady = 15 , ipadx = 10)

window.mainloop()
