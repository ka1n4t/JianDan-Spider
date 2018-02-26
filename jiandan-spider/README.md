# 爬取煎蛋网上的妹子图：http://jandan.net/ooxx

#### 环境：
    python版本：3.6.4
    库：urllib和BeautifulSoup

#### 原理：
    获取图片真实url，并将图片下载到downloads文件夹，每3s下载一张

#### 参数说明：
    -h: 帮助文档<br>
    -p: 爬取的页数，默认为1。当页数大于1时使用多线程
    
#### 参考：
    爬虫:
        http://blog.csdn.net/van_brilliant/article/details/78723878
        https://github.com/van1997/JiandanSpider
    多线程:
        https://www.cnblogs.com/cnkai/p/7504980.html
        https://www.cnblogs.com/yanfengt/p/6305542.html
