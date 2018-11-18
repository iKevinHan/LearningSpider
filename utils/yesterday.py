
import datetime
nowtime=datetime.datetime.now()
deltaday=datetime.timedelta(days=1)
yesterday=nowtime-deltaday
print(yesterday.strftime('%Y-%m-%d'))
print(nowtime.strftime('%Y-%m-%d'))
# data = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# print(data)
