
import urllib, urllib2, re
from bs4 import BeautifulSoup

def getSeriesTitle(chapterOrSeriesURL):
	'''
	gets title of chapter from KissManga chapter URL.
	Example: http://kissmanga.com/Manga/Uzumaki/Uzumaki-Chapter-20?id=56954
	'''
	domainURL = 'kissmanga.com/Manga/'
	remainingString = chapterOrSeriesURL.split(domainURL)[-1]
	seriesTitle = remainingString.split('/')[0]
	return seriesTitle



def scrapeChapter(chapterURL):
	'''
	scrapes an entire chapter from the given URL of the KissManga domain
	downloads as multiple png's
	'''
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]


	source = opener.open(chapterURL).read()


	## example link:
	## http://2.bp.blogspot.com/-ANiS2T94Sdg/VfF1NJY6kEI/AAAAAAAC2qw/nVbQGfhTVbI/s16000-Ic42/000.png
	for link in re.findall('http://.*[0-9][0-9][0-9].png', source):
	    cleanLink = link


	    ## the code above just prints the link;
	    ## if you want to actually download, set the flag below to True

	    actually_download = True
	    if actually_download:
	        filename = cleanLink.split('/')[-1]
	        urllib.urlretrieve(cleanLink, 'Images/' + filename)

def scrapeSeries(seriesURL):
	'''
	<a href="/Manga/Uzumaki/Uzumaki-Chapter-2?id=56786" title="Read Uzumaki Uzumaki Chapter 002 online">Uzumaki Chapter 002</a>
	'''
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	source = opener.open(seriesURL).read()

	seriesTitle = getSeriesTitle(seriesURL)

	prefixString = '<a href="/Manga/' + seriesTitle
 	htmlLines = [line for line in source.split("\n") if line.startswith(prefixString)]
 	chapterRelativeURLs = [line.split('\"')[1] for line in htmlLines]

 	chapterPrefixString = 'http://kissmanga.com'
 	chapterURLs = [chapterPrefixString + line for line in chapterRelativeURLs]

 	for chapterURL in chapterURLs:
 		scrapeChapter(chapterURL)
	# TODO finish this method

scrapeSeries('http://kissmanga.com/Manga/Uzumaki')
# scrapeChapter('http://kissmanga.com/Manga/Toriko/Ch-338--Joa-VS-Midora--?id=241108')



