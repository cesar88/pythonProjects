import requests
import json
import datetime
import pandas
from pprint import pprint
import matplotlib.pyplot as plt

url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2019-09-05"

r = requests.get(url).text
js = json.loads(r)
data = js["bpi"]
fix_json = []

def get_day_name(date_value):
    return datetime.datetime.strptime(date_value, '%Y-%m-%d').strftime('%A')


for key in data:
    fix_json.append({"date": key,
                     "value": data[key],
                     "day": get_day_name(key)
                     })

df = pandas.DataFrame(fix_json)
df["t+1"] = df["value"].shift(1)
df.fillna(0, inplace=True)
df["diff"] = (df["value"]-df["t+1"])/df["t+1"]

df["kadir_way"] = list(df.value.pct_change())
days = list(set(df.day))

create_db=[]
for i in days:
    z=df[df.day==i]
    create_db.append({"day":i,
                      "std":z.kadir_way.describe()["std"]})

newdf=pandas.DataFrame(create_db)
# print(newdf)gün bazlı standart sapma
z=pandas.date_range(start='2013-01-01',end='2019-01-01',freq='M')
date_df=pandas.DataFrame({"start_date":z})
date_df["end_date"]=date_df.shift(-1)#son tarih baş tarihin yanında olsun diye alt alta gelmesin herşey diye

s={str(date_df.iloc[14])["start_date"]}
e={str(date_df.iloc[14])["end_date"]}



print(date_df)

ax = plt.gca()
df.plot(kind='line',
        x='date',
        y='value',
        color='red',
        ax=ax)
plt.show()