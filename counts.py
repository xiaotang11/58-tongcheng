#Author :Mary Tang
import time
from page_parsing import url_list

while True:
    print(url_list.find().count())  #url_list是数据库中的表
    time.sleep(5)