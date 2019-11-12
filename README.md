# python_for_fun
> My name is Sophia, a student in a Chinese High School. Now I am 17 years old on grade 12. I really love computer science and data analysis, so I did some side projects here..

[![Build Status][travis-image]][travis-url]

My two major projects contain getting information from two Chinese websites -- a housing website and a social website -- by utilizing crawler and also data visualization by python .

![](header.png)

## Installation

Please install Python 3 before run the script

```sh
python xx.py
```


## Abstract
 World Wide Web has incorporated to people’s daily lives and people are able to acquire the information they need online by simply typing few key words in the search box. However, for those users who require to access an general area with a specific criteria, such work is impossible because data is not in a managed and structured architecture across the web. Therefore, in terms of dealing with tremendous database, there are several tools we can employ for data mining, including crawler which is a preferable and effortless way to salvage data from webs. Additionally, for those people who deal with data everyday, data visualization can benefit them a lot. This paper presents two systematic project: one for the crawler in website www.lianjia.com, a Chinese housing website like Redfin. The other one is the visualization of the friends information in WeChat which is the Chinese social network like Facebook.


## Demo Video
[![python-geo locations visualization
](https://img.youtube.com/vi/fTK3uYI_TXo/sddefault.jpg)](https://www.youtube.com/watch?v=fTK3uYI_TXo)

[![python-sex ratio visualization
](https://img.youtube.com/vi/L7p8S6ffhzM/sddefault.jpg)](https://www.youtube.com/watch?v=L7p8S6ffhzM)

[![python-weChat auto reply
](https://img.youtube.com/vi/KqwYfzCA1rs/sddefault.jpg)](https://www.youtube.com/watch?v=KqwYfzCA1rs)

[![python-lianjia city crawler
](https://img.youtube.com/vi/qU3I0_uwuUI/sddefault.jpg)](https://www.youtube.com/watch?v=qU3I0_uwuUI)

## Usage example

 If I want to get the Top Ten Movie names in a social website, I can type codes as following:

```sh
from urllib.request  import urlopen
from bs4 import BeautifulSoup
url = "https://movie.douban.com/top250?start=0&filter=" #go to the html page
html = urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
grid_view_first= soup.find("ol",attrs={'class':'grid_view'}) #find the div
lis = grid_view_first.find_all("li")
for li in lis:
    span= li.find("span",class_="title")
    print(span.string) #get the names of movies
```

By processing this code, we can successfully get all the top ten movie names for use.
As for another project, we can visualize certain attributes of friends in social media, such as sex ratio or geographic location.


## Paper
![Paper](paper.jpg?raw=true " Crawler and data visualization by python ")


## Meta
Sophia -- 243681509@qq.com
[https://github.com/YUNZHANG123/python_life_fun]
