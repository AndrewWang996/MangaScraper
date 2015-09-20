
import urllib, urllib2, re

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

## example link:
## http://2.bp.blogspot.com/-ANiS2T94Sdg/VfF1NJY6kEI/AAAAAAAC2qw/nVbQGfhTVbI/s16000-Ic42/000.png

# source = urllib.urlopen('http://kissmanga.com/Manga/Toriko/Ch-338--Joa-VS-Midora--?id=241108').read()
source = opener.open('http://kissmanga.com/Manga/Toriko/Ch-338--Joa-VS-Midora--?id=241108').read()

# print(source)

## every image name is an abbreviation composed by capital letters, so...
for link in re.findall('http://.*[0-9][0-9][0-9].png', source):
    cleanLink = link


    ## the code above just prints the link;
    ## if you want to actually download, set the flag below to True

    actually_download = True
    if actually_download:
        filename = cleanLink.split('/')[-1]
        urllib.urlretrieve(cleanLink, 'Images/' + filename)

'''
from bs4 import BeautifulSoup
import requests
r  = requests.get('http://kissmanga.com/Manga/Toriko/Ch-338--Joa-VS-Midora--?id=241108')

data = r.text

print(data)

soup = BeautifulSoup(data)

print(soup)
'''