# -*- coding: utf-8 -*-

import uvicorn
from spider import Spider
from fastapi import FastAPI
from threading import Timer
from threading import Thread

data_zhihu = []     #知乎
data_tieba = []     #贴吧
data_baidu = []     #百度
data_vsite = []     #V2EX
data_bsite = []     #B站
data_weibo = []     #微博

s = Spider()

def run_tieba():
    global data_tieba
    data_tieba = s.spider_tieba()
def run_zhihu():
    global data_zhihu
    data_zhihu = s.spider_zhihu()
def run_vsite():
    global data_vsite
    data_vsite = s.spider_vsite()
def run_weibo():
    global data_weibo
    data_weibo = s.spider_weibo()

def run_bsite():
    global data_bsite
    data_bsite = s.spider_bsite()

#此组15分钟采集一次
def task1():
    #多线程运行
    Thread(target=run_zhihu,).start()
    Thread(target=run_tieba,).start()
    Thread(target=run_weibo,).start()
    Thread(target=run_vsite,).start()
    Timer(15*60,task1,).start()

#此组每天采集一次
def task2():
    #多线程运行
    Thread(target=run_bsite,).start()
    Timer(24*60*60,task2,).start()

task1()
task2()

app = FastAPI()
@app.get("/")
def index():
    return {'hello':'world!'}

@app.get("/hot/{name}")
def read_name(name: str):
    if name == 'zhihu':
        return data_zhihu
    elif name == 'vsite':
        return data_vsite
    elif name == 'weibo':
        return data_weibo
    elif name == 'tieba':
        return data_tieba
    elif name == 'bsite':
        return data_bsite

if __name__ == '__main__':
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=80)

    

