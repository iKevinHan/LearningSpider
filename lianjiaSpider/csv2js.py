import csv

reader=csv.reader(open('syfj.csv'))
for row in reader:
    loc=row[1]
    sloc=loc.split(',')
    lng=''
    lat=''
    if len(sloc)==2:#第一行是列名需要做判断
        lng=sloc[0]
        lat=sloc[1]
        count=row[5]
        out='{\"lng\":'+lng+',\"lat\":'+lat+',\"count\":'+count+'},'
        print(out)

#
# import csv
# csvfile = open("yyy.csv", 'w')
# csvwrite = csv.writer(csvfile)
# fileHeader = ["id", "score"]
# d1 = ["1", "100"]
# d2 = ["2", "80"]
# csvwrite.writerow(fileHeader)
# csvwrite.writerow(d1)
# csvwrite.writerow(d1)
# csvfile.close()
#
#
# import csv
# add_info = ["3", "70"]
# csvFile = open("yyy.csv", "a")
# writer = csv.writer(csvFile)
# writer.writerow(add_info)
# csvFile.close()
#
# import csv
# data = open("xxx.csv",'r')
# dict_reader = csv.DictReader(data)
# for i in dict_reader:
#     print (i)
# #>>> {'score': '100', 'id': '1'}
# #>>> {'score': '80', 'id': '2'}
#
# import csv
# data = open("xxx.csv",'r')
# dict_reader = csv.DictReader(data)
# col_score = [row['score'] for row in dict_reader]

        # cj = http.cookiejar.CookieJar()
        # pro = urllib.request.HTTPCookieProcessor(cj)
        # opener = urllib.request.build_opener(pro)
        # urllib.request.install_opener(opener)

import requests
s = requests.Session() #创建一个session对象
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
# 结果
# '{"cookies": {"sessioncookie": "123456789"}}'

import requests
s = requests.Session()
#设置session对象的auth属性，用来作为请求的默认参数
s.auth = ('user', 'pass')
#设置session的headers属性，通过update方法，将其余请求方法中的headers属性合并起来作为最终的请求方法的headers
s.headers.update({'x-test': 'true'})
# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
#结果
{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic dXNlcjpwYXNz", #
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.4",
    "X-Test2": "true",  #
    "X-Text": "true" #
  }
}


import requests
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'

import requests
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)
