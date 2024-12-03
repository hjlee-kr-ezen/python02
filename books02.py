import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas

# chrome 드라이버 설정
chrome_options = Options()
chrome_options.add_argument('--headless') #브라이저를 열지않음
chrome_options.add_argument('--disable-gpu') #gpu비활성화

# chrome 드라이버 서비스설정
service = Service(ChromeDriverManager().install())
# webdriver 초기화
driver = webdriver.Chrome(service=service)

# 교보문고 월간 베스트셀러 페이지 url
url = "https://store.kyobobook.co.kr/bestseller/total/monthly"

# 웹페이지 열기
driver.get(url)

# 페이지 로딩을 위한 대기 (최대 10초)
wait = WebDriverWait(driver, 10)

# 책정보를 크롤링
books = []
for i in range(1,21):
    try:
        if i<=10:
            title_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/a')))
        else:
            title_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/a')))
        title = title_element.text

        if i<=10:
            author_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/div[2]')))
        else:
            author_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/div[2]')))
        author = author_element.text

        if i<=10:
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/div[3]/div/span[2]/span[1]')))
        else:
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/div[3]/div/span[2]/span[1]')))
        price = price_element.text

        books.append([title, author, price])
    except Exception as e:
        print(f"Error fetching data for book {i}:{e}")
        continue #예외발생시 for문으로 돌아가라

#크롬 드라이버 종료
driver.close() # driver.quit()

# 데이터 저장 (pandas DataFrame)
df = pandas.DataFrame(books, columns=["Title", "Author", "Price"])

# CVS 파일로 저장
df.to_csv("kyobo_best_sellers_monthly.csv", encoding="utf-8-sig", index=False)

# DataFrame 출력
print(df)
