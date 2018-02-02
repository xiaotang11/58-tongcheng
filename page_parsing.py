#Author :Mary Tang

import requests
from bs4 import BeautifulSoup
import time
import pymongo   #这个库用来帮助链接mongodb数据库

client = pymongo.MongoClient('localhost',27017)  #链接mongo数据库
ceshi = client['ceshi']   #给数据库起名ceshi，  注意要用【】
url_list = ceshi['url_list3']   #在数据库ceshi中创建表url_list3
item_info = ceshi['item_info3']  #在数据库ceshi中创建表item_info3

#spider1 获取每一个类目的链接，同事将每一个类目的列表页的url获取下来

def get_links_from(channel,pages,who_sells=0):
    #person      http://cd.58.com/pbdn/0/pn2/
    #shangjia    http://cd.58.com/pbdn/1/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))#拼接链接
    wb_page = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_page.text,'lxml')
    if soup.find('td','t'): #如果，页面中有td这个标签，我们就认为这个页面有内容，否则就是没有商品了
        l = soup.select('td.t a.t') #得到列表页的所有url
        for link in l:
            item_link = link.get('href').split('?')[0]  #整理一下该链接，去处多余的部分
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass


#spider2 爬取商品详细信息
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exit = '404' in soup.find('script',type='text/javascript').get('src').split('/')
    #判断是否是404页面
    if no_longer_exit:
        pass
    else:
        title = soup.title.text
        price = soup.select('.price')[0].text  #实际这个列表中只有一个元素
        location = list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        time = soup.select('.mtit_con_left .time')[0].text #实际这个列表中只有一个元素
        item_info.insert_one({'title':title,'price':price,'location':location,'time':time})#插入到数据库中
        print({'title':title,'price':price,'location':location,'time':time})
        # print(time)

# get_item_info('http://cd.58.com/pingbandiannao/27792525402190x.shtml')



# get_link_from('http://cd.58.com/tongxunyw/',1)




