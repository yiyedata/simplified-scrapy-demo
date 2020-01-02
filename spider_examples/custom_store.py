from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_scrapy.core.redis_urlstore import RedisUrlStore
from simplified_scrapy.core.utils import appendFile
import os,json
class CustomStore():
  _objFilename='data/{}_custom.json'
  def __init__(self, name):
    self._objFilename=self._objFilename.format(name)
    if(not os.path.exists('data/')):
      os.mkdir('data/')
  def saveObj(self, data):
    objs = data.get("Datas")
    if(objs != None):
      if(objs):
        appendFile(self._objFilename, json.dumps(objs,ensure_ascii=False))
    elif isinstance(data, dict):
      appendFile(self._objFilename, json.dumps(data,ensure_ascii=False))

class ToscrapeSpider(Spider):
  name = 'toscrape.com'
  allowed_domains = ['toscrape.com/']
  start_urls = ['http://quotes.toscrape.com/']
  # refresh_urls = True # For debug. If efresh_urls = True, start_urls will be crawled again.

  # Storing URLs with redis
  url_store = RedisUrlStore(name,{'host':'127.0.0.1','port':6379})
  obj_store = CustomStore(name)

  def extract(self, url, html, models, modelNames):
    doc = SimplifiedDoc(html)
    divs = doc.getElements('div',attr="class",value='quote')
    data = []
    for div in divs:
      data.append({
        'text':div.getElementByClass('text').text,
        'author':div.getElementByClass('author').text,
        'tags':[a.text for a in div.div.getElementsByTag('a')]
      })
    nextA = doc.getElementByClass('next')
    if nextA:
      nextA = nextA.listA(url=url['url'])
    return {"Urls": nextA, "Data": data}

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ToscrapeSpider())