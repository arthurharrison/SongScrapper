import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://www.google.com/")
print(html.read())
