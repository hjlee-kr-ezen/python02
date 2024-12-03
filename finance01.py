import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas



# chrome 드라이버 서비스설정
service = Service(ChromeDriverManager().install())
# webdriver 초기화
driver = webdriver.Chrome(service=service)

url = "https://finance.naver.com/marketindex/"
driver.get(url)
driver.switch_to.frame("frame_ex1")

# 파싱 및 태그추출
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
result = []
currencys = soup.select("body > div > table > tbody > tr")

for data in currencys:
    country = data.select("td.tit > a")[0].text.strip()
    exchange = data.select("td.sale")[0].text
    result.append([country, exchange])

driver.close()

df = pandas.DataFrame(result, columns = ["통화명", "환율"])
#CSV
df.to_csv("환율정보.csv", encoding="utf-8-sig", index=False)