#  TO know How to use  : https://youtu.be/j3RPjjpc8HE
import socket
import subprocess


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


print('"User Should  Make Sure You Are Running this From The Folder Which You Want to Share\nAnd Do Not Close this '
      'Window until File Transfer Completes" \n')
ip = get_ip_address()
print(ip)
hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
print("HOST Name is: " + hostname, '\n')
print("WARNING :  MAKE SURE YOUR OTHER DEVICE CONNECTED TO THE SAME WIFI ROUTER")
print(" ")
url = ip + ':8000'
print("Open Browser In Your Other Device and Type ", url, ' in URL Box')
print('\nKindly Ignore Upcoming Lines\n\n')
cmd = 'python -m http.server 8000'
returned_value = subprocess.call(cmd, shell=True)
