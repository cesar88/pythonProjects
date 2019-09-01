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
z = df[df.day == "Monday"]
print(z.kadir_way.describe())
exit()


days = list(set(df.day))

for i in days:
    print(i)
    z = df[df.day == i]
    print(z.value.describe()["mean"])

exit()
ax = plt.gca()
df.plot(kind='line',
        x='date',
        y='value',
        color='red',
        ax=ax)
plt.show()