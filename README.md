# python_for_fun
> My name is Sophia, a student in a Chinese High School. Now I am 17 years old on grade 12. I really love computer science and data analysis, so I did some side projects here..

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

My two major projects contain getting information from two Chinese websites -- a housing website and a social website -- by utilizing crawler and also data visualization by python .

![](header.png)

## Demo Video

[![Alt text](https://youtu.be/MdwB-z4eIBs0.jpg)](https://youtu.be/MdwB-z4eIBs)


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


## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki


