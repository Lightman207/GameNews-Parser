# This is Game News Parser v1.0

## *How to setup?*

+ Install last Python version [here](https://www.python.org/downloads/)
+ Install Library in your project 
```pip install requests, beautifulsoup4```
+ Clone repository in your directory
+ That's all, have fun :heart:
## *How it works*

### You can parsing game news sites
#### To do this, you need to: 
1) import in your project
```python
import module as pars
from time import sleep
```
2) Add this code
```python
# waiting before request
waitTime = 3

howMaPages = 3 # it's how many pages you want to parse

for i in range(1, howMaPages): 
    sleep(waitTime)
    # Stop Game
    url = 'https://stopgame.ru/news/all/p' + str(i) 
    pars.parseSite(url, '_content_11mk8_159', 'a', '_title_11mk8_60')
    # GameMag
    url = 'https://gamemag.ru/news/page/' + str(i) 
    pars.parseSite(url, 'news-item__text-wrapper', 'a', 'news-item__text')
    # VGTimes
    url = 'https://vgtimes.ru/page/' + str(i) 
    pars.parseSite(url, 'item-name type0', 'span', '')
```
3) If you want to add another site in your parser, just add it in loop , you can use these two lines of code
```python
    # Stop Game
    url = 'https://stopgame.ru/news/all/p' + str(i) # This's URL on your site, with page but without nomber of page
    pars.parseSite(url, '_content_11mk8_159', 'a', '_title_11mk8_60') # firs argument is's url to site | second argument it's where your div with title location | third argument it's your title attribute | fourth argument it's attribute class
```
4) Now you need to get your parsed info, to do this you need call the function ``getInfo()`
```python
    getInfo('data/text.txt') #This's folder where you want to save your parsed data
```
## What features are in development?
+ Function `getInfo()` only creating .txt file with parsed data, but we want to this function can give you dictionary with all parsed data. It's first what we want to change in our project
+ The second and most important thing we want to do is to make sure that you can filter out duplicate news when parsing a lot of news sites
## How you can help us?
Use it, star it, share it :heart:
