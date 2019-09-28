# Goal：To get all the city name in website lianjia
# Purpose: practise beautifulsoup
# Sophia  20190914

# filename: citys.py
# coding: utf-8
import sys

import csv

from urllib.request  import urlopen
from bs4 import BeautifulSoup

url = "https://www.lianjia.com"

# get html page
html = urlopen(url).read()

# get BeautifulSoup subjective，
# pip install lxml
bsobj = BeautifulSoup(html, "lxml")

# get all <a> tag under div class="fc-main clear"  
city_tags = bsobj.find("div", {"class":"fc-main clear"}).findChildren("a")



# save every data in the file "citys.csv"
with open("./cityslian.csv", "w") as f:
    writ = csv.writer(f)
    for city_tag in city_tags:
        # get the href link of <a> tag
        city_url = city_tag.get("href").encode("utf-8")
        # get the names of <a> tag
        city_name = city_tag.get_text()
        print(city_name)
        print(city_url)
        writ.writerow((city_name, city_url))
        
