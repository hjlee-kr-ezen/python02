import pymongo
import requests
import datetime
from bs4 import BeautifulSoup


def naver_news_section(sid):
    #뉴스 분야(sid)를 입력하면 제목, 링크를 리스트로 추출하는함수
    url = f"https://news.naver.com/section/{sid}"
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(html.text, "lxml")
    #find_all("태그이름", "클래스이름") -> 태그이름과 클래스이름이 매칭되는것을 찾는다.
    headline_list = soup.find_all("strong", "sa_text_strong")
    headline_press = soup.find_all("div", "sa_text_press")
    headline_link = soup.find_all("a", "sa_text_title")
    print(headline_list)
    print(headline_press)
    print(headline_link)
    print(len(headline_list))
    print(len(headline_press))
    print(len(headline_link))
    title_lst = []
    press_lst = []
    link_lst = []
    date_lst = []
    section_lst = []
    nowDate = datetime.datetime.now()
    for title in headline_list:
        title_lst.append(title.text)
        date_lst.append(nowDate.strftime("%Y%m%d"))
        section_lst.append(f"{sid}")
    for press in headline_press:
        press_lst.append(press.text)
    for link in headline_link:
        link_lst.append(link["href"])

    resultList = [{"title": title, "press": press, "link": link, "date": date, "section": section}
        for title, press, link, date, section
        in zip(title_lst, press_lst, link_lst, date_lst, section_lst)]
    print(resultList)
    return resultList
    

resultList = naver_news_section(101)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb1"]
mycol = mydb["news"]
x = mycol.insert_many(resultList)
print(x.inserted_ids)
myclient.close()