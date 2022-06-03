from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = int(input('Enter position: '))
times = int(input('Enter times: '))
url = 'http://py4e-data.dr-chuck.net/known_by_Heddle.html'

while times > 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position-1]
    url = url.get('href', None)
    times -= 1

tag = tags[position-1]
name = tag.contents[0]
print(name)