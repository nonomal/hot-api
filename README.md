# hot-api

### 演示网站：

网址 `http://cx.lookcos.cn`
请求方法，直接访问 ：
http://cx.lookcos.cn/hot/zhihu  获取知乎热门
http://cx.lookcos.cn/hot/vsite  获取V站热门

### 启动方法：

执行`python hotapi.py` 即可

### 说明：

1.使用fastapi框架，多线程定时分组爬取网站，高效简单。
2.闲着没事，发现了这个框架，拿来玩玩，只写了后端，没写前端。

### 数据格式：

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/json.jpg)

### 响应速度：

响应速度均在30ms以内，毕竟是提前抓取好的数据直接调用，看图。

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/zhihu.jpg)

![avatar](https://raw.githubusercontent.com/LookCos/hot-api/master/Preview/vsite.jpg)
