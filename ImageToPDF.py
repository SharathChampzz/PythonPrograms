#Steps Followed :
#Open Image --> Convert to RGB --> Make a list of all images --> save 1st image in list by appending other images too.

from PIL import Image
from os import listdir , getcwd

dir = input('Paste Directory Location here , which contains images : ')
loc = dir.replace("\\","\\\\")

imagelist = []
for image in listdir(dir):
	imgPath = dir + '\\' + image
	#print(imgPath)
	img = Image.open(imgPath).convert('RGB')
	imagelist.append(img)

OutputName = input('Enter Output PDF Name : ')
if OutputName.endswith('.pdf') is False:  # No extension found
	OutputName = OutputName + '.pdf'	

im1 = imagelist[0]
imagelist.pop(0)
im1.save(OutputName , save_all= True , append_images=imagelist)


print(f'Saved! PDF at {getcwd()}')
