# -*- coding: utf-8 -*-

st = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Cookie: Hm_lvt_c32eb45d9f69afbc206e06d63e668e75=1540891445; PHPSESSID=1hs9pg8v9d5fmi0v51i49rf6t6; Hm_lpvt_c32eb45d9f69afbc206e06d63e668e75=1540891811
Host: www.chinacourt.org
If-Modified-Since: Thu, 25 Oct 2018 03:14:32 GMT
If-None-Match: W/"5bd13518-65fa"b
Referer: https://www.chinacourt.org/courtlist/list/id/MzA0MDaAAgA%3D.shtml
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
'''
for i in st.split('\n'):
    if i:
        if i.startswith(':'):
            i = i[1:]
            i = i.replace(':', "':'", 1)
            i = ':' + i
        else:
            i = i.replace(':', "':'", 1).replace(' ','',1)
        i = "'" + i + "'" + ","

        print(i)
