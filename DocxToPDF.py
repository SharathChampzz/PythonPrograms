# pip install docx2pdf
from docx2pdf import convert
print('Converting..')
source = r"C:\Users\SHARATH KUMAR H K\Desktop\Projects\OFC\front sheet.docx"  # docx file location 
#print(source)

destination = source.replace('.docx','.pdf')

convert(source , destination)
print('\nConverted Successfully!!\n')
print(f'File Sucessfully Saved as {destination}')
