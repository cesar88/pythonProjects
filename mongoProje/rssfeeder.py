import xmltodict,requests,pymongo


connection=pymongo.MongoClient("mongodb://167.71.72.44:27017")
db=connection["bilgeadam"]
table=db["fatih_ahaber"]

url = "https://www.ahaber.com.tr/rss/anasayfa.xml"
r = requests.get(url)
xmlData=r.text
jsonData= xmltodict.parse(xmlData)

for data in jsonData["rss"]["channel"]["item"]:
    print(data["title"])
    print(data["link"])
    table.insert_one({"Title":data["title"],"Link":data["link"]})

