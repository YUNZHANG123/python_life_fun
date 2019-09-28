# Goal：To get the name of some movies in douban website page.
# Purpose: practise beautifulsoup
# Sophia  20190914
# -*- coding: utf-8 -*-

from urllib.request  import urlopen
from bs4 import BeautifulSoup
#go to the html page
url = "https://movie.douban.com/top250?start=0&filter="
html = urlopen(url).read()

soup = BeautifulSoup(html,"lxml")
grid_view_first= soup.find("ol",attrs={'class':'grid_view'}) #find the div


lis = grid_view_first.find_all("li")

for li in lis:
    span= li.find("span",class_="title")
    print(span.string) #get the names of movies

	




