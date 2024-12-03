import requests
from bs4 import BeautifulSoup

#res = requests.get("https://store.kyobobook.co.kr/bestseller/total/monthly")
res = requests.get("https://www.yes24.com/Product/Category/BestSeller?CategoryNumber=001&sumgb=06")
html = res.content
book = BeautifulSoup(html, "html.parser")

best = book.select(".gd_name")
#print(best)
for tag in best:
    print(tag)

writer_list = book.select(".info_auth")
#print(best)
for tag in writer_list:
    print(tag)

price_list = book.select(".info_price>strong>em")
#print(best)
for tag in price_list:
    print(tag)

for title, author, price in zip(best, writer_list, price_list):
    title_text = title.text.strip()
    #author_text = author.
    price_text = price.text.strip()
    print(title_text, price_text)