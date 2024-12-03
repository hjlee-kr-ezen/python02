import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chrome 드라이버 서비스설정
service = Service(ChromeDriverManager().install())
# webdriver 초기화
driver = webdriver.Chrome(service=service)

url = "https://www.naver.com"
driver.get(url) # 네이버페이지 열기
input_tag = driver.find_element(By.CSS_SELECTOR, "#query") # 네어버 검색창이동
input_tag.send_keys("보넥도") # 검색어 입력
input_tag.send_keys("\n") # enter key 입력
driver.implicitly_wait(3) # 3초간 대기

input("브라우저를 닫으려면 Enter를 누르세요..")
driver.close()