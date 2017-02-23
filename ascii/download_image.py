import urllib
import ssl
url = 'https://latimesherocomplex.files.wordpress.com/2014/07/sm_sailormoon_05-0.jpg'
context = ssl._create_unverified_context()
sailor_moon = urllib.urlretrieve(url, "sailor_moon.jpg", context=context)

sailor_moon
