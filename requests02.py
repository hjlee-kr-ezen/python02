import requests

parameters = {"code": "005930"}
res = requests.get("https://finance.naver.com/item/main.naver",
                    params=parameters)
print(res.url)
print(res.text)