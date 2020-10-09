# This will work Only if Account is Public Not on Private Accounts
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def downloader(photo_url):
    #extract some character of photo_url in order to name the photo 
    import os
    photo_name = '' + photo_url[-25:-6]
    if not os.path.isdir('Downloads'):
    	os.mkdir('Downloads')
    pat = os.path.join(os.getcwd(), 'Downloads')
    requests_url = requests.get(photo_url)
    if 'jpg' in photo_url:
    	f = open(os.path.join(pat, photo_name + '.jpg'), 'ab')
    else:
    	f = open(os.path.join(pat, photo_name + '.mp4'), 'ab')
    f.write(requests_url.content)
    print('Processing...')
    f.close()
    print('Download complete')


def extract_url(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html5lib')
	# print(soup.prettify())
	try:
		video_url = soup.find("meta", property="og:video")
		download_url = video_url['content']
		print('Video Found!')
	except:
		photo_url = soup.find("meta", property="og:image")
		download_url = photo_url['content']
		print('Image Found!')
	# print(download_url)
	downloader(download_url)

url = input('Enter URL : ')
extract_url(url)
