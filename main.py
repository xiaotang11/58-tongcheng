#Author :Mary Tang

from multiprocessing import Pool  #该库帮助电脑调用主机的多个内核
from channel_extract import channel_list #引入这个list表
from page_parsing import get_links_from


#自动添加页码
def get_all_links_from(channel):
    for num in range(1,100): #我们默认为只有100页
        get_links_from(channel,num)


if __name__ == '__main__':
     #创建进程池
    pool = Pool()  #创建一个进程池，所有的函数都会自动扔到这个池子里，Pool(process=6)，可以这样配置进程，默认没有process
    # 时，会自动分配，分析内核
    pool.map(get_all_links_from,channel_list.split()) #get_all_links_from函数依次作用于channellist里面的url，返回所有的links






