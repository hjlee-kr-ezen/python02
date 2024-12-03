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
chrome_options.add_argument('--headless') #브라우저를 열지않음
chrome_options.add_argument('--disable-gpu') #gpu비활성화

# chrome 드라이버 서비스설정
service = Service(ChromeDriverManager().install())
# webdriver 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://hometax.go.kr/websquare/websquare.html?w2xPath=/ui/pp/index_pp.xml&tmIdx=43&tm2lIdx=4306000000&tm3lIdx=4306080000"
driver.get(url)
time.sleep(3) # 3초 대기

# 사업자등록번호 엑셀파일 읽어오기
resultList = []
df = pandas.read_excel("사업자등록번호.xlsx")

for no in df["business_no"]:
    driver.find_element(By.CSS_SELECTOR, "#mf_txppWframe_bsno").send_keys(no)
    driver.find_element(By.CSS_SELECTOR, "#mf_txppWframe_trigger5").click()
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "#mf_txppWframe_grid2_cell_0_1 > nobr").text
    resultList.append(result)

driver.close()
#조회결과저장
df["result"] = resultList
df.to_excel("사업자등록번호 조회결과.xlsx",index=False)