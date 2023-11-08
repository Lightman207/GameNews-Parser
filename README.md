# GameNews-Parser

```python
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
```
