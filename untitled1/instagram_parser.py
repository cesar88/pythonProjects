import requests
import json

def instagram_lib(instagram_isim):
    url="https://www.instagram.com/{}/?__a=1".format(instagram_isim)
    rs = requests.get(url)
    page= json.loads(rs.text)
    img_lib=[]
    for p in page["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
        # img_lib.append(p["node"]["display_url"])
        img_lib.append({"img":p["node"]["display_url"]})
    return img_lib
