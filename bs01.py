import requests
from bs4 import BeautifulSoup

html_txt = """
<p class='wether' id='tw'>오늘의 날씨</p>
<h1>한때 소나기가 내리겠습니다.</h1>
"""
#파싱, 분석가능한 데이터형태로 변환
soup = BeautifulSoup(html_txt,"html.parser")
tag = soup.find("p") #p태그를 찾아서 tag변수에 저장
print(tag)      #p태그전체내용
print(tag.name) #태그의 이름 => p
print(tag.attrs) #태그 속성 출력
print(tag.attrs["class"]) #class속성 값
print(tag.attrs["id"]) #id속성 값
print(tag.text) #태그내 값(시작태그와 끝태그안의 값)