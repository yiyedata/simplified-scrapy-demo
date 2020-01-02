from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_scrapy.core.mongo_urlstore import MongoUrlStore
from simplified_scrapy.core.mongo_htmlstore import MongoHtmlStore
from simplified_scrapy.core.mongo_objstore import MongoObjStore
class ToscrapeSpider(Spider):
  name = 'toscrape.com'
  allowed_domains = ['toscrape.com/']
  start_urls = ['http://quotes.toscrape.com/']
  # refresh_urls = True # For debug. If efresh_urls = True, start_urls will be crawled again.

  # Storing URL with mongodb
  url_store = MongoUrlStore(name,{'host':'127.0.0.1','port':27017})
  # Storing html with mongodb 
  html_store = MongoHtmlStore(name,{'host':'127.0.0.1','port':27017})
  # Storing Obj with mongodb 
  obj_store = MongoObjStore(name)

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