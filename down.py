import requests
import json
#伪造浏览器下载图片
res = requests.get(
    url="https://movie.douban.com/j/subject_abstract?subject_id=36284589",
    headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}
)
jasonres = res.text
jasonres = json.loads(jasonres)

subject = jasonres['subject']

for key,value in subject.items():
    if key == 'title' :
        name = value
    if key == 'url':
        url = value
print("名称：{} 地址：{}".format(name,url))

import re
from bs4 import BeautifulSoup
page = 0
while page<2:
    page += 1
    url = "https://www.chinaunicom.com/43/menu01/1/column05?pageNo={}&pageSize=10&year=2022&month=".format(page)

    res = requests.get(
       url=url,
       headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}
    )
    if not res:
        break


jasonres = res.text
f = open("test.txt","wb")
#f.write(jasonres.encode("utf-8"))

obj = BeautifulSoup(jasonres,'html.parser')

divare = obj.find('div',attrs={'class':'template-list-text'})
trare = divare.find_all('tr')
for tr in trare:
    if not tr:#防止是广告位 空的
        continue
    print(tr.text)
    num = re.findall("\d+-\d+-\d+",tr.text)
    print(num)
    test = tr.text+"\n"
    f.write(test.encode("utf-8"))


f.close()
