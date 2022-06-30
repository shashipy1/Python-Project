from typing import Mapping
from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, massage):
    notification.notify(
        title = title,
        message = massage,
        app_icon = "E:\All Programming\project\CoronaCases\image.ico",
        timeout = 10

    )

def getData(url): 
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("Shashi", "let's stop the speard of this virus togrther")
    myHtmlData = getData('https://www.mohfw.gov.in/')
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myDatastr = ""



    # for the print of table data
    # for table in soup.find_all('table'):
    #     print(table)
    


    # for tr data
    for td in soup.find_all('tbody')[0].find_all('td'):
        print(td.get_text())



        # myDatastr += td.get_text()
        # print(myDatastr.split("\n\n"))
    # myDatastr = myDatastr[1:]for tr in soup.find_all('tr')[2]:
    # itemList = myDatastr.split("\n\n")
    # for item in itemList:
        # print(item.split("\n"))



 
