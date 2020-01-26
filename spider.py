# -*- coding: utf-8 -*-

import json
import requests
from lxml import etree
from threading import Timer

vsite_api = "https://www.v2ex.com/?tab=hot"
bsite_api = 'https://www.bilibili.com/ranking/all/0/0/1'
weibo_api = "https://s.weibo.com/top/summary?cate=realtimehot"
tieba_api = "http://tieba.baidu.com/hottopic/browse/topicList?res_type=1"
zhihu_api = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

#组装数据
def packdata(para_data):
    list_data = []
    for i in para_data:
        data = {}
        data["title"]=i[0]
        data["url"]=i[1]
        list_data.append(data)
    return list_data
    
class Spider(object):
    def __init__(self,url=None):
        if url!=None:
            self.url = url
            self.res = requests.get(url,headers=headers)
            self.res.encoding = "utf-8"
            self.soup = etree.HTML(self.res.text)

    #知乎热榜
    def spider_zhihu(self):
        
        list_zhihu = [] #此列表用于储存解析结果
        res = Spider(zhihu_api).res  
        #逐步解析接口返回的json
        zhihu_data = json.loads(res.text)['data']
        for part_zhihu_data in zhihu_data:              #遍历每一个data对象
            zhihu_id = part_zhihu_data['target']['id']    #从对象得到问题的id
            zhihu_title = part_zhihu_data['target']['title'] #从对象得到问题的title
            list_zhihu.append([zhihu_title,zhihu_id])          #将id 和title组为一个列表，并添加在list_zhihu列表中
        return packdata(list_zhihu)
    
    #微博热搜
    def spider_weibo(self):
        list_weibo = [] #此列表用于储存解析结果
        weibo = "https://s.weibo.com"
        soup = Spider(weibo_api).soup
        for soup_a in soup.xpath("//td[@class='td-02']/a"):
            wb_title = soup_a.text
            wb_url = weibo + soup_a.get('href')
            #过滤微博的广告，做个判断
            if "javascript:void(0)" in wb_url:
                pass
            else:
                list_weibo.append([wb_title,wb_url])
        return packdata(list_weibo)


    #贴吧热度榜单
    def spider_tieba(self):
        list_tieba = []
        soup = soup = Spider(tieba_api).soup
        for soup_a in soup.xpath("//a[@class='topic-text']"):
            tieba_title = soup_a.text
            tieba_url = soup_a.get('href')
            list_tieba.append([tieba_title,tieba_url])
        return packdata(list_tieba)


    #V2EX热度榜单
    def spider_vsite(self):
        list_v2ex = []
        vsite ="https://www.v2ex.com"
        soup = Spider(vsite_api).soup
        for soup_a in soup.xpath("//span[@class='item_title']/a"):
            vsite_title = soup_a.text
            vsite_url = vsite+soup_a.get('href')
            list_v2ex.append([vsite_title,vsite_url])
        return packdata(list_v2ex)

    #B站排行榜
    def spider_bsite(self):
        list_bsite = []
        soup = Spider(bsite_api).soup
        for i in soup.xpath("//div[@class='info']/a"):
            bsite_title = i.xpath('text()')[0]
            bsite_url = i.get('href')
            list_bsite.append([bsite_title,bsite_url])
        return packdata(list_bsite)
        
Spider().spider_bsite()

