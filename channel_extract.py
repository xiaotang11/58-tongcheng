#Author :Mary Tang
#获取58同城不同类目的url链接
import requests
from bs4 import BeautifulSoup

start_url = 'http://cd.58.com/sale.shtml'
url_host = 'http://cd.58.com'

# def get_channel_urls(url):
#     wb_data = requests.get(start_url)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#
#     links = soup.select('#ymenu-side > ul li > b > a ')
#     for link in links:
#         page_url = url_host+link.get('href') #获取各个类目的链接
#
#         print(page_url)



# get_channel_urls(start_url)

channel_list = '''
    http://cd.58.com/tongxunyw/
    http://cd.58.com/danche/
    http://cd.58.com/fzixingche/
    http://cd.58.com/diandongche/
    http://cd.58.com/sanlunche/
    http://cd.58.com/peijianzhuangbei/
    http://cd.58.com/diannao/
    http://cd.58.com/bijiben/
    http://cd.58.com/pbdn/
    http://cd.58.com/diannaopeijian/
    http://cd.58.com/zhoubianshebei/
    http://cd.58.com/shuma/
    http://cd.58.com/shumaxiangji/
    http://cd.58.com/mpsanmpsi/
    http://cd.58.com/youxiji/
    http://cd.58.com/jiadian/
    http://cd.58.com/dianshiji/
    http://cd.58.com/ershoukongtiao/
    http://cd.58.com/xiyiji/
    http://cd.58.com/bingxiang/
    http://cd.58.com/binggui/
    http://cd.58.com/chuang/
    http://cd.58.com/ershoujiaju/
    http://cd.58.com/bangongshebei/
    http://cd.58.com/diannaohaocai/
    http://cd.58.com/bangongjiaju/
    http://cd.58.com/ershoushebei/
    http://cd.58.com/yingyou/
    http://cd.58.com/yingeryongpin/
    http://cd.58.com/muyingweiyang/
    http://cd.58.com/muyingtongchuang/
    http://cd.58.com/yunfuyongpin/
    http://cd.58.com/fushi/
    http://cd.58.com/nanzhuang/
    http://cd.58.com/fsxiemao/
    http://cd.58.com/xiangbao/
    http://cd.58.com/meirong/
    http://cd.58.com/yishu/
    http://cd.58.com/shufahuihua/
    http://cd.58.com/zhubaoshipin/
    http://cd.58.com/yuqi/
    http://cd.58.com/tushu/
    http://cd.58.com/tushubook/
    http://cd.58.com/wenti/
    http://cd.58.com/yundongfushi/
    http://cd.58.com/jianshenqixie/
    http://cd.58.com/huju/
    http://cd.58.com/qiulei/
    http://cd.58.com/yueqi/
    http://cd.58.com/chengren/
    http://cd.58.com/nvyongpin/
    http://cd.58.com/qinglvqingqu/
    http://cd.58.com/qingquneiyi/
    http://cd.58.com/chengren/
    http://cd.58.com/xiaoyuan/
    http://cd.58.com/ershouqiugou/
    http://cd.58.com/tiaozao/
    http://cd.58.com/tiaozao/
    http://cd.58.com/tiaozao/
'''