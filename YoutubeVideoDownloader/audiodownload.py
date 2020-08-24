import subprocess

u = input('Enter URL : ')

if '=' in u:
	u = u.split('=')[-1]
else:
	u = u.split('/')[-1]

cmd = "py -3 -m youtube_dl --restrict-filenames --ignore-errors -x --audio-format mp3 "  + u
print(cmd)
subprocess.call( cmd , shell=True , cwd = 'C:/Users/SHARATH KUMAR H K/Desktop/Songs/YoutubeAudios')