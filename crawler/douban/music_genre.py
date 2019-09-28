# Goal：To get some music genres in douban website page.
# Purpose: practise beautifulsoup
# Sophia  20190914
# -*- coding: utf-8 -*-

from urllib.request  import urlopen
from bs4 import BeautifulSoup
#go to the html page
url = "https://music.douban.com/"
html = urlopen(url).read() #read the html
soup = BeautifulSoup(html,"lxml") #apply beautifulsoup
music_genre = soup.find(attrs={'class':'popular-artists section'}) #go to the div 
genres = music_genre.find_all("p",attrs={'class':'genre'}) #get the names of music genre
for genre in genres:
    print(genre.string)


		

		