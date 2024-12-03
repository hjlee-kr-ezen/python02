import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome 드라이버 서비스설정
service = Service(ChromeDriverManager().install())
# webdriver 초기화
driver = webdriver.Chrome(service=service)

url="https://www.naver.com"
driver.get(url)
print(driver.current_url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
tag_list = soup.select("body p")
for tag in tag_list:
    print(tag.text)

driver.close()