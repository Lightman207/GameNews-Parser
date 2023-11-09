import requests
from bs4 import BeautifulSoup
from time import sleep


titleList = []
urlList = []
spisNews = []
spisUrl = []


# Parse info
headers = {"User-Agent": 
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

def parseSite(url, divLocation, titleAtr, titleClass):
    url3 = []
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    block = soup.findAll("div", class_=divLocation)

    for i in block:
        title = i.find(titleAtr, class_=titleClass).text
        href = i.find(titleAtr, class_=titleClass).get('href')

        url2 = url.rpartition('.ru')[0]
        url2 = str(url2) + '.ru' + str(href)

        titleList.append(title)
        urlList.append(str(url2))
    


def getInfo(fileLocation):
    txt = 'None'
    file = open(fileLocation, 'a', encoding="utf=8")
    count = 0
    try:
        for element in titleList:
            count += 1

            txt = str(titleList[count])
            urlTxt = str(urlList[count])
            file.write(txt + ' | ' + urlTxt + "\n")
    except IndexError: 
        print("You parsed all news in data file")
    file.close
    return spisUrl, spisNews