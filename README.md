# hot-api


### 详情 请转到我的博客看  https://www.lookcos.cn/?p=466


### 演示网站：

网址 `http://cx.lookcos.cn`

请求方法，直接访问 ：

http://cx.lookcos.cn/hot/zhihu  获取知乎热门

http://cx.lookcos.cn/hot/vsite  获取V站热门

### 特点：

1.多线程，能以迅雷不及掩耳之势完成对任务的抓取

2.任务分组进行，有些网站更新频率高（如微博，百度热搜等），而有些网站只需要每天抓取一次。

3.使用python3 `threading.Timer`模块实现非阻塞定时任务。

4.使用 fastapi框架，配合uvicorn，效率高。


### 说明：

1.无聊。

2.闲着没事，发现了这个框架，拿来玩玩，只写了后端，没写前端。

### 启动方法：

执行`python hotapi.py` 即可


### 数据格式：

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/json.jpg)


### 响应速度：

响应速度均在30ms以内，毕竟是提前抓取好的数据直接调用，看图。

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/zhihu.jpg)

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/vsite.jpg)
