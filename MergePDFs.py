#To merge PDF files in a same directory in order
from PyPDF2 import PdfFileMerger, PdfFileReader    #pip install PyPDF2
import os

mergedObject = PdfFileMerger() # create the PdfFileMerger object
 
dir = r"C:\Users\SHARATH KUMAR H K\Desktop\Projects\DC\event2"   # Directory location of PDF files

for pdf in os.listdir(dir): 					# Loop through all of the pdf in directory and append their pages
 	PdfName = dir + '\\' + pdf  				# Getting Full path for PDF
 	mergedObject.append(PdfFileReader(PdfName, 'rb'))

# Write all the files into a file which is named as shown below
OutputName = input('Enter Output PDF Name : ')
if OutputName.endswith('.pdf') is False:  # No extension found
	OutputName = OutputName + '.pdf'  # so add extension by yourself
mergedObject.write(OutputName)
print(f'Saved! PDF at {os.getcwd()}')
