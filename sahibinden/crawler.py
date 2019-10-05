from wsgiref import headers

import requests
from bs4 import BeautifulSoup
import settings
import pymongo
import re


connection=pymongo.MongoClient("mongodb://167.71.72.44:27017")

db=connection["bilgeadam"]

def get_total_number(main_url):
    url = "https://www.arabam.com/ikinci-el/otomobil/alfa-romeo?take=50"
    r = requests.get(url=url, headers=settings.HEADERS_GET).text
    # print(r)
    linkList = []
    soup = BeautifulSoup(r, "html.parser")
    sayi = soup.find_all("span",{"class":"color-red4 bold pl4 fz13"})[0].text
    sayi=re.findall("\d+",sayi)[0]
    page_count=int(sayi) / 50
    total_page_number=round(page_count)
    return total_page_number

def get_all_car_link():
    url ="https://www.arabam.com/ikinci-el/otomobil/alfa-romeo?take=50"
    r = requests.get(url=url, headers=settings.HEADERS_GET).text
    page=get_total_number(url)
    # print(r)
    linkList = []
    soup = BeautifulSoup(r,"html.parser")
    for i in range(0,page):
        main_url="https://www.arabam.com/ikinci-el/otomobil/alfa-romeo?take=50&page=[]".format(i)
        for link in soup.find_all('a',{"class":"listing-text-new word-break"}):
            linkList.append(settings.MAIN_URL+link["href"])
    return linkList

for link in get_all_car_link():
    r=requests.get(url=link,headers=settings.HEADERS_GET).text
    soup=BeautifulSoup(r,"html.parser")
    data_list=[]
    for information in soup.find_all("div",{"class":"banner-column-detail bcd-mid-extended p10 bg-white"}):
        for i in range(2,15):
            field = information.select("#js-hook-for-observer-detail > div.banner-column-detail.bcd-mid-extended.p10.bg-white > ul > li:nth-child(6) > span.bli-particle.bold")
            field= field[i].lstrip()
            value = information.select("#js-hook-for-observer-detail > div.banner-column-detail.bcd-mid-extended.p10.bg-white > ul > li:nth-child(6) > span:nth-child(2)")
            value = value.replace("\xa0", "").replace("\n", "").lstrip().rstrip()
            data_list.append({field: value})

    # r=requests.get(url=link,headers=settings.HEADERS_GET).text
    # soup=BeautifulSoup(r,"html.parser")
    # aa= soup.find_all('classifiedDetail',' div.classifiedDetail')
    # print(link)

# sağ  tıklayıp seç selector diyerek chrome dan alınır
    # classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > span



exit()

url="https://www.sahibinden.com/ilan/vasita-otomobil-alfa-romeo-2011-model-1.6-jtd-cam-tavanli-ciulietta-muayene-yeni-kacirma-730857849/detay";
r=requests.get(url=url,headers=settings.HEADERS_GET).text
soup=BeautifulSoup(r,"html.parser")
data_list=[]
for information in soup.find_all("ul",{"class":"classifiedInfoList"}):
    for i in range(2,20):
        field=information.select("#classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > strong")
        field=field[i].lstrip()
        value=information.select("#classifiedDetail > div.classifiedDetail > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > span")
        value=value.replace("\xa0","").replace("\n","").lstrip().rstrip()
        data_list.append({field:value})
print(data_list)





