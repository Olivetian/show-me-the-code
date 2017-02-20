#encoding = utf-8

# an HTML file, find the body inside.

import urllib2
from bs4 import BeautifulSoup

url = "http://www.google.com.hk"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")
data = soup.find('body')
print data


