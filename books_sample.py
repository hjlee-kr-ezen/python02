from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# 크롬 드라이버 설정 (headless 모드)
chrome_options = Options()
chrome_options.add_argument('--headless')  # headless 모드 (브라우저를 띄우지 않음)
chrome_options.add_argument('--disable-gpu')  # GPU 비활성화 (일부 환경에서 필요)

# 드라이버 경로 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 교보문고 베스트셀러 페이지 URL
url = "https://store.kyobobook.co.kr/bestseller/online/daily"

# 웹 페이지 열기
driver.get(url)

# 페이지 로딩을 위한 대기 (최대 10초)
wait = WebDriverWait(driver, 10)

# 책 정보 크롤링
books = []
for i in range(1, 21):  # 첫 20위까지 크롤링 (예: 베스트셀러 목록)
    try:
        # 책 제목
        if i<=10:
            title_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/a')))
        else:
            title_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/a')))
        title = title_element.text

        # 책 저자
        if i<=10:
            author_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/div[2]')))
        else:
            author_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/div[2]')))
        author = author_element.text
        
        # 책 가격
        if i<=10:
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[1]/li[{i}]/div/div[2]/div[2]/div[3]/div/span[2]/span[1]')))
        elif i==14 | i==15:
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/div[3]/div/span/span[1]')))
        else:
            price_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[{i-10}]/div/div[2]/div[2]/div[3]/div/span[2]/span[1]')))
        price = price_element.text

        
        books.append([title, author, price])
    except Exception as e:
        print(f"Error fetching data for book {i}: {e}")
        continue

author_element = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[1]/main/section/div/div/section/ol[2]/li[4]/div/div[2]/div[2]/div[2]')))  
print(author_element)
# 크롬 드라이버 종료
driver.quit()

# 데이터 저장 (pandas DataFrame 사용)
df = pd.DataFrame(books, columns=["Title", "Author", "Price"])

# CSV 파일로 저장
df.to_csv("kyobo_best_sellers_daily.csv", index=False)

# DataFrame 출력
print(df)
