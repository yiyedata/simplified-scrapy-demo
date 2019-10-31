"""
采集例子，自动抽取文章数据
"""
from simplified_scrapy.core.spider import Spider 
# from simplified_scrapy.core.redis_urlstore import RedisUrlStore
# from simplified_scrapy.core.mongo_objstore import MongoObjStore

class DemoSpider(Spider):
  name = 'demo-spider'
  start_urls = ['http://www.scrapyd.cn/']
  models = ['auto_main','auto_obj']

  # Storing URLs with redis, if you don't like this, please comment it out 
  # url_store = RedisUrlStore(name,{'host':'127.0.0.1','port':6379})
  # Storing Objs with mongodb, if you don't like this, please comment it out 
  # obj_store = MongoObjStore(name,{'host':'127.0.0.1','port':27017})
  def urlFilter(self,url):
    # 过滤掉视频数据采集
    return url.find('/shipin/')<0
  def afterResponse(self, response, url):
    html = Spider.afterResponse(self, response, url)
    return Spider.removeScripts(self, html)
