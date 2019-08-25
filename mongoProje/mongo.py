import pymongo


connection=pymongo.MongoClient("mongodb://167.71.72.44:27017")

db=connection["bilgeadam"]
tablo=db["fatih"]
ornek_veri={"sehir":"İzmir"}
#
data= tablo.find_one( {"sehir" : ornek_veri["sehir"]})



toplu_veri=[{"sehir":"Çorum"},
            {"sehir":"Eskişehir"},
            {"sehir":"Edirne"}]


tablo.delete_one(ornek_veri)



def insertWithControl(ornek_veri):
    if data == None:
        tablo.insert_one(ornek_veri)
        print("Insert")
    else:
        print("Veri Var" +ornek_veri)


def insertMany(toplu_veri):
    tablo.insert_many(toplu_veri)


def deleteVeri(veri):
    tablo.delete_one(veri)


# data=tablo.find()
#
# for veri in data:
#     print(veri)

