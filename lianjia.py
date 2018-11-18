# -*- coding: utf-8 -*-

import requests
import re
import time

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# 调用service 酱，推送到微信
def send_msg(title, info):
    url = 'https://pushbear.ftqq.com/sub?sendkey=5058-7ea8146946e5bb0e4fadfc15864b4776&text=%s&desp=%s' \
          % (title, info)
    requests.get(url)


def get_station():
    # 12306的城市名和城市代码js文件url
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061'
    r = requests.get(url, verify=False)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)' # \u4e00-\u9fa5是所有汉字的unicode编码范围
    result = re.findall(pattern, r.text) # 按正则表达式规则匹配
    station = dict(result)
    return station


# 生成查询的url
def get_query_url(text):
    # 城市名代码查询字典
    # key：城市名 value：城市代码

    try:
        date = '2018-08-18'
        from_station_name = '上海'
        to_station_name = '北京'
        from_station = text[from_station_name] # 将城市名转换为城市代码
        to_station = text[to_station_name]
    except:
        date, from_station, to_station = '--', '--', '--'

    # api url 构造
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    print(url)

    return url


# 获取车次信息
def query_train_info(url, text):

    try:
        r = requests.get(url, verify=False)

        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']

        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = text['上海']
            # 终点站
            to_station_code = data_list[7]
            to_station_name = text['北京']
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'

            # 打印查询结果
            info = (
            '车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n座位情况：\n一等座：「{}」 \n二等座：「{}」\n软卧：「{}」\n硬卧：「{}」\n硬座：「{}」\n无座：「{}」\n\n'.format(
                train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

            print(info)
            if (second_class_seat and second_class_seat!= '无' and train_no == "G102"):
                # send_msg("G102次高铁二等座有票了", info)
                return True
            else:
                continue

    except Exception as e:
        print(e)


text = get_station()
print(text)
url = get_query_url(text)

# 循环查询，直到查询到想要的车次有票终止
while True:
    time.sleep(1) # 刷票频率
    if query_train_info(url, text):
        break