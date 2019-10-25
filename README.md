# simplified-scrapy-demo
simplified scrapy demo
# Requirements
+ Python 2.7, Python 3+
+ pip install simplified-scrapy
+ Works on Linux, Windows, Mac OSX, BSD
``
如果是Python 2需要安装futures
`pip install futures`
# 运行
进入项目根目录，执行下面命令  
`python start.py`
# Demo
文件夹demo_spiders下，为爬虫例子。爬虫类需要继承Spider类。
```
from core.spider import Spider 
class DemoSpider(Spider):
```
需要给爬虫定义一个名字，配置入口链接地址，与抽取数据用到的模型名称。下面是采集新浪健康资讯数据的一个例子。其中auto_main_2表示抽取相同2级域名的链接，auto_obj表示自动抽取页面中的资讯数据，包括标题、正文和时间。
```
name = 'demo-spider'
start_urls = ['http://health.sina.com.cn/']
models = ['auto_main_2','auto_obj']
```
其中模型文件在文件夹models下，如果需要自定义模型，可以使用这个模型工具，[下载地址](https://github.com/yiyedata/yiyespider/raw/master/publish/yiyeclient_0.9.zip)。使用说明在[这里](https://github.com/yiyedata/yiyespider/raw/master/%E4%B8%80%E4%B8%9A%E5%88%86%E5%B8%83%E5%BC%8F%E9%80%9A%E7%94%A8%E9%87%87%E9%9B%86%E7%B3%BB%E7%BB%9F%E6%A8%A1%E5%9E%8B%E5%B7%A5%E5%85%B7%E6%96%87%E6%A1%A3.docx)
# 自定义抽取
除了使用配置模型的方式抽取数据外，也可以自定义抽取数据，如例子中的 extractSpider.py。自定义抽取时，需要重写下面的方法
`def extract(self, url, html, models, modelNames):`  
返回的数据格式如下
`[{"Urls": lst, "Data": data}]`
其中，Urls为链接数据，会存放在链接表；Data为抽取出的目标数据，会存放在对象表。
自定义抽取时，系统提供了如下几个方法
```
def listA(html,url=None,start=None,end=None):
def listImg(html,url=None,start=None,end=None):
def getElementByID(id,html,start=None,end=None):
def getElementAttrByID(id,attr,html,start=None,end=None):
def getElementTextByID(id,html,start=None,end=None):
def getElementByTag(tag,html,start=None,end=None):
def getElementByClass(className,html,start=None,end=None):
def getElementsByTag(tag,html,start=None,end=None):
def getElementsByClass(className,html,start=None,end=None):
def getElementBy(attr,value,html,start=None,end=None):
```
# Spider类有下面这些方法和属性可以重写
```
concurrencyPer1s = 1#默认值
use_cookie = True#默认值
use_ip = False#全局设置#默认值
version = "0.0.1"#默认值
self.start_urls = []#默认值
self.url_store = SqliteUrlStore(self.name)#默认值
self.html_store = SqliteHtmlStore(self.name)#默认值
self.cookie_store = SqliteCookieStore()#默认值
self.obj_store = ObjStore(self.name)#默认值
def beforeRequest(self, request):
def afterResponse(self, response, cookie, url):
def downloadError(self,url,err=None):
def saveObj(self, data):
def urlFilter(self, url):
def extract(self, url,html,models,modelNames):
def plan(self):
```
# CookieStore类需要实现下面这些方法
```
def getCookie(self, url):
def setCookie(self, url, cookie):
```
# HtmlStore类需要实现下面这些方法
```
def popHtml(self,state=0):
def saveHtml(self,url,html):
def updateState(self,id,state):
```
# UrlStore类需要实现下面这些方法
```
def popUrl(self):
def getCount(self):
def checkUrl(self,url):
def saveUrl(self, urls,i=None):
def resetUrls(self, urls):
```
# Setting
自定义的爬虫需要在配置文件（setting.json）进行配置，配置后爬虫类才会生效。
```
{
  "spiders":[
    {"file":"spiders.extractSpider","class":"ExtractSpider"}
  ],
  "concurrency":1,
  "concurrencyPer1S":6,
  "intervalTime":0.3
}
```

