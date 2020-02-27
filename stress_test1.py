from simplified_scrapy import SimplifiedMain, Spider
from simplified_scrapy.core.sqlite_requesttm import SqliteRequestTm
from simplified_scrapy.core.sqlite_urlstore import SqliteUrlStore
import random
class StressTest(Spider):
  name = 'stress_test'
  request_tm = True # 启用统计记录
  concurrencyPer1s=5
  request_timeout=60
  save_html = False # 不保存页面数据
  base_url = "http://quotes.toscrape.com/"
  url_store = SqliteUrlStore(name, {'duplicateRemoval':False})
  def __init__(self):
    self.start_urls = []
    for i in range(self.concurrencyPer1s*2):
      self.start_urls.append(self.base_url+"#"+str(random.randint(0,100000)))
    self.clearUrl()
    Spider.__init__(self,self.name) #necessary
  def extract(self,url,html,models,modelNames):
    urls = [{"url":url.url}] # Repeated requests
    if(urls):
      return {"Urls":urls}
    return True

SimplifiedMain.statistics=SqliteRequestTm('stress_test',setting={'port':8787})
SimplifiedMain.statistics.clearRecode() # Delete last stress test result
SimplifiedMain.statistics.startRecode() # Start up recode
SimplifiedMain.statistics.startServer() # Start up web server, http://localhost:8787
SimplifiedMain.startThread(StressTest()) # Start stress test