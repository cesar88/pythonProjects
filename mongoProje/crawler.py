from wsgiref import headers

import requests
from bs4 import BeautifulSoup
import settings
import pymongo


connection=pymongo.MongoClient("mongodb://167.71.72.44:27017")

db=connection["bilgeadam"]

def get_all_car_link():
    url ="https://www.sahibinden.com/alfa-romeo?pagingSize=50"
    r = requests.get(url=url,headers = settings.HEADERS_GET).text
    # print(r)
    linkList = []
    soup = BeautifulSoup(r,"html.parser")
    print(soup)
    for link in soup.find_all('a',{"class":"classifiedTitle"}):
        linkList.append(settings.MAIN_URL+link["href"])
    return linkList


# for link in get_all_car_link():
    # r=requests.get(url=link,headers=settings.HEADERS_GET).text
    # soup=BeautifulSoup(r,"html.parser")
    # aa= soup.find_all('classifiedDetail',' div.classifiedDetail')
    # print(link)

# sağ  tıklayıp seç selector diyerek chrome dan alınır
    # classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > span
url="https://www.sahibinden.com/ilan/vasita-otomobil-alfa-romeo-2011-model-1.6-jtd-cam-tavanli-ciulietta-muayene-yeni-kacirma-730857849/detay";
r=requests.get(url=url,headers=settings.HEADERS_GET).text
soup=BeautifulSoup(r,"html.parser")
data_list=[]
for information in soup.find_all("ul",{"class":"classifiedInfoList"}):
    for i in range(2,20):
        field=information.select("#classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > strong")
        field=field.lstrip()
        value=information.select("#classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > span")
        value=value.replace("\xa0","").replace("\n","").lstrip().rstrip()
        data_list.append({field:value})
print(data_list)





