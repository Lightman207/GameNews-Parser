import modules as pars
from time import sleep

# waiting before request
waitTime = 3
it = 0

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
pars.getInfo('data/text.txt')
