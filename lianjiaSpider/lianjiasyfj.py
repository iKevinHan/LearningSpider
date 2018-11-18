from bs4 import BeautifulSoup
import requests
import csv
import re
def getlocation(name):#调用百度API查询位置
    bdurl='http://api.map.baidu.com/geocoder/v2/?address='
    output='json'
    ak='你的密匙'#输入你刚才申请的密匙
    ak='VMfQrafP4qa4VFgPsbm4SwBCoigg6ESN'#输入你刚才申请的密匙
    callback='showLocation'
    uri=bdurl+name+'&output=t'+output+'&ak='+ak+'&callback='+callback+'&city=沈阳'
    print (uri)
    res=requests.get(uri)
    s=BeautifulSoup(res.text)
    lng=s.find('lng')
    lat=s.find('lat')
    if lng:
        return lng.get_text()+','+lat.get_text()

url='https://sy.lianjia.com/ershoufang/pg'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}#请求头，模拟浏览器登陆
page=list(range(0,101,1))
p=[]
hi =[]
fi=[]
for i in page:#循环访问链家的网页
    response=requests.get(url+str(i),headers=header)
    soup=BeautifulSoup(response.text)
    #提取价格
    prices=soup.find_all('div',class_='priceInfo')
    for price in prices:
        p.append(price.span.string)

    #提取房源信息
    hs=soup.find_all('div',class_='houseInfo')
    for h in hs:
        hi.append(h.get_text())

    #提取关注度
    followInfo=soup.find_all('div',class_='followInfo')
    for f in followInfo:
        fi.append(f.get_text())
    print(i)

print (p)
print (hi)
print (fi)
#houses=[]#定义列表用于存放房子的信息
n=0
num=len(p)
# file=open('da.csv', 'w', newline='',encoding='utf-8')
file=open('syfj.csv', 'w', newline='')
headers = ['name', 'loc', 'style', 'size', 'price', 'foc']
writers = csv.DictWriter(file, headers)
writers.writeheader()
while n<num:#循环将信息存放进列表
    h0=hi[n].split('|')
    name=h0[0]
    loc=getlocation(name)
    style = re.findall(r'\s\d.\d.\s', hi[n])#用到了正则表达式提取户型
    if style:
        style=style[0]
    size=re.findall(r'\s\d+\.?\d+',hi[n])#用到了正则表达式提取房子面积
    if size:
        size=size[0]
    price=p[n]
    foc=re.findall(r'^\d+',fi[n])[0]##用到了正则表达式提取房子的关注度
    house = {
        'name': '',
        'loc': '',
        'style': '',
        'size': '',
        'price': '',
        'foc': ''
    }
    #将房子的信息放进一个dict中
    house['name']=name
    house['loc']=loc
    house['style']=style
    house['size']=size
    house['price']=price
    house['foc']=foc
    try:
        writers.writerow(house)#将dict写入到csv文件中
    except Exception as e:
        print (e)
        # continue
    n+=1
    print(n)
file.close()