from bs4 import BeautifulSoup

html_txt = """
<html>
<head>
<title>BS4 page</title>
</head>
<body>
<h1 class="portal_cls">검색포털</h1>
<p>
<a href="https://www.daum.net">다음 바로가기</a><br>
<a href="https://www.naver.com">네이버 바로가기</a>
</p>
<a href="https://www.google.com" class="alink_cls">구글</a>
<a target="_테스트_">테스트</a>
<p class="footage_cls" id="company">2021, ABC Company</p>
<p class="footage_cls" id="addr">Korea</p>
</body>
</html>
"""
soup = BeautifulSoup(html_txt, "html.parser")
tag = soup.select_one("h1") # 조건에 맞는 태그 하나만 가지고 온다.
print(tag.text)

tag_list = soup.select("h1") # 조건에 맞는 태그 리스트형태로 가져온다.
for tag in tag_list:
    print(tag.text)

tag_list = soup.select("a") # 조건에 맞는 태그 리스트형태로 가져온다.
for tag in tag_list:
    print(tag.text)

print("="*50)
tag_list = soup.select("p > a")
for tag in tag_list:
    print(tag.text)

print("="*50)
tag_list = soup.select(".footage_cls")
for tag in tag_list:
    print(tag.text)

print("="*50)
tag_list = soup.select("#company")
for tag in tag_list:
    print(tag.text)

print("="*50)
#a 태그중 href속성이 있는 태그만 리스트에 저장
tag_list = soup.select("a[href]")
for tag in tag_list:
    print(tag.text, tag.attrs["href"])