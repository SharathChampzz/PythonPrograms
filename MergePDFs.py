from PyPDF2 import PdfFileMerger, PdfFileReader
import os
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
dir = r"C:\Users\SHARATH KUMAR H K\Desktop\Projects\DC\event2"

# Loop through all of the pdf in directory and append their pages
for pdf in os.listdir(dir):
 	PdfName = dir + '\\' + pdf
 	mergedObject.append(PdfFileReader(PdfName, 'rb'))

# I had 116 files in the folder that had to be merged into a single document

#for fileNumber in range(1, 117):
    
 
# Write all the files into a file which is named as shown below
OutputName = input('Enter Output PDF Name : ')
if OutputName.endswith('.pdf') is False:  # No extension found
	OutputName = OutputName + '.pdf'
mergedObject.write(OutputName)

print(f'Saved! PDF at {os.getcwd()}')
print('Done!')