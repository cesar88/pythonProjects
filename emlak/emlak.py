import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import time
import settings

class HurriyetParser:

    main_url =settings.MAIN_URL;

    def __init__(self):
        

    def main_links():
        liste = []
        for i in range(10):
            url = "https://www.hurriyetemlak.com/ankara-satilik?page={}".format(i)
            r = requests.get(url=url, headers=settings.HEADERS_GET).text
            time.sleep(6)
            soup = BeautifulSoup(r, "html.parser")
            for item in soup.find_all("a", class_="overlay-link"):
                if "http" not in item["href"]:
                    liste.append(main_url + item["href"])

        return (liste)

    def cleaning(liste):
        returnList=[]
        for word in liste:
            word = word.lstrip().rstrip().replace("'", "").replace(" ", "")
            word=(word.split("="))
            returnList.append(returnList)
        return returnList

    def get_info(url):
        labels = []
        values = []
        r = requests.get(url=url, headers=settings.HEADERS_GET).text
        soup = BeautifulSoup(r, "html.parser")
        text = str(soup.find_all("script")[5])

        labels=["city","town","neighborhood","realestatecategory","realestatetype","adtype","ownertype","totalvalue","roomtype","m2","heatingtype","buildingage"
            ,"floor","addate","fuelType","registerID"]

        values=[]
        for item in labels:
            values.append(re.findall(item.join(" =.*'"))[0])

        return dict(zip(cleaning(labels),cleaning(values)))


s = time.time()
data = []
for link in main_links():
    data.append(get_info(link))
pprint(data)
b = time.time()

print(b-s)