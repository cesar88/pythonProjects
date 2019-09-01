import newspaper

url = 'https://www.mynet.com.tr'
news =newspaper.build(url)

# for item in news.articles:
#     print(item.url)


for category in news.category_urls():
    print(category)