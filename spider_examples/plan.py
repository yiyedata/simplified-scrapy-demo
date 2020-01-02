from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_scrapy.request import req
from datetime import datetime
class ToscrapeSpider(Spider):
  name = 'toscrape.com'
  allowed_domains = ['toscrape.com/']
  start_urls = ['http://quotes.toscrape.com/']

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
  
  # If you want to collect start_urls regularly, override this method.
  # It returns an array of hours and minutes
  def plan(self):
    if datetime.now().weekday()>=6: # Except for weekends
      return []
    else:
      return [{'hour':8,'minute':30},{'hour':18,'minute':0}]

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ToscrapeSpider())