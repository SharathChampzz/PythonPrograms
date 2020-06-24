import cv2
from time import sleep

total = int(input('How Many Images you would like to capture : '))
videoCaptureObject = cv2.VideoCapture(0)
imgcount = 0
print('Starting in 3 seconds...')
sleep(3)
try:
	while(True):
	    ret,frame = videoCaptureObject.read()
	    path = r'Dataset\starting\trial' 
	    cv2.imwrite(path + '\\' + str(imgcount) + '.JPG' , frame)  # First Create folder
	    cv2.imshow('Capturing Video',frame)
	    imgcount += 1
	    print(f'Images Taken  : {imgcount}')
	    if imgcount == total:
	    	print(f'{imgcount} images are Saved! Thank you!')
	    	break
	    print('Change!')
	    if(cv2.waitKey(1) & 0xFF == ord('q')):
	        videoCaptureObject.release()
	        cv2.destroyAllWindows()
	    sleep(3)
except Exception as e:
	print(e)