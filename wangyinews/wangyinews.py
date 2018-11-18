'''
网易新闻的评论实际上没有它所标注的页数这么多
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyquery import PyQuery as pq
import pymongo

# 配置数据库信息
Mongo_URL = 'localhost'
Mongo_DB = 'wangyiNews'
MONGO_COLLECTION = 'comments_pinduoduo'
client = pymongo.MongoClient(Mongo_URL)
db = client[Mongo_DB]

# 创建浏览器对象、等待时间对象
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# 网易新闻评论url
# 在拼多多里，折叠着一个最真实的中国
url = 'http://comment.tie.163.com/DODJBOE900018M4D.html'


def search():
    print('正在检索')
    try:
        # 等待页面全部加载完毕
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.wrapper .main-bg.clearfix #tie-main .tie-foot .post-tips'))
        )
        html = driver.page_source  # 返回页面源码
        return html
    except TimeoutException:  # 超时异常
        return search()

def parse_one_page(html):
    doc = pq(html)
    items = doc('.tie-new .list-bdy .trunk.clearfix').items()
    for item in items:
        comments = {
            'name': item.find('.rgt-col .tie-author.clearfix .author-info .from').text(),
            'ip': item.find('.rgt-col .tie-author.clearfix .author-info .ip').text(),
            'date': item.find('.rgt-col  .tie-author.clearfix .post-time').text()[2:].replace('\n', ''),
            'comment': item.find('.rgt-col .tie-bdy .tie-cnt').text(),
            'support': item.find('.rgt-col .tie-operation.clearfix .rgt .support').text().replace('\n', '').replace('顶', ''),
            'digg': item.find('.rgt-col .tie-operation.clearfix .rgt .digg').text().replace('\n', '').replace('踩', '')
        }
        print(comments)
        save_to_mongo(comments)
    next_page()
    time.sleep(5)

def next_page():
    # 翻页操作
    try:
        '#tie-main > div.tie-new > div.list-foot.clearfix > div > ul > li:nth-child(6) > span'
        '//*[@id="tie-main"]/div[3]/div[3]/div/ul/li[6]/span'
        if wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.wrapper .main-bg.clearfix #tie-main .tie-new .list-foot.clearfix .page-bar .m-page .next.z-enable'))):
            next_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.wrapper .main-bg.clearfix #tie-main .tie-new .list-foot.clearfix .page-bar .m-page .next.z-enable')))
            next_page.click()
    except TimeoutException:
        return None

def save_to_mongo(comments):
    try:
        if db[MONGO_COLLECTION].insert(comments):
            print('存储到MONGODB成功')
    except  Exception:
        print('存储到MONGODB失败')

def main():
    driver.get(url)
    time.sleep(5)
    try:
        for i in range(68):  # 观察实际的评论页数
            print(i)
            html = search()
            parse_one_page(html)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 网易新闻最后一页必须将页面下拉至底端才能输出
    finally:
        time.sleep(5)
        driver.close()


if __name__ == '__main__':
    main()