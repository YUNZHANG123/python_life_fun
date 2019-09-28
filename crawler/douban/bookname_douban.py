# Goal：To get the name of some books in douban website page.
# Purpose: practise beautifulsoup
# Sophia  20190914
# -*- coding: utf-8 -*-

from urllib.request  import urlopen
from bs4 import BeautifulSoup

url = "http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book"

# get html page
html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

book_div = soup.find(attrs={"id":"book"})

book_a = book_div.findAll(attrs={"class":"title"})
for book in book_a:
    print(book.string)