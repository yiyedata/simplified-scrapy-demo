from simplified_scrapy import SimplifiedMain, Spider
from simplified_scrapy.core.sqlite_requesttm import SqliteRequestTm
from simplified_scrapy.core.sqlite_urlstore import SqliteUrlStore
import random
class StressTest(Spider):
  name = 'stress_test'
  request_tm = True 
  concurrencyPer1s=5
  request_timeout=60
  save_html = False # Do not save page data
  base_url = "http://quotes.toscrape.com/"

  def popUrl(self):
    if(self.checkConcurrency()):
      self._downloadPageNum=self._downloadPageNum+1
      return {'url':self.base_url}
    else:
      return {}

  def urlCount(self):
    return 1
  
  def extract(self,url,html,models,modelNames):
    return True

SimplifiedMain.statistics=SqliteRequestTm('stress_test',setting={'port':8787})
SimplifiedMain.statistics.clearRecode() # Delete last stress test result
SimplifiedMain.statistics.startRecode() # Start up recode
SimplifiedMain.statistics.startServer() # Start up web server, http://localhost:8787
SimplifiedMain.startThread(StressTest()) # Start stress test
