from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_scrapy.request import req
class ToscrapeSpider(Spider):
  name = 'toscrape.com'
  allowed_domains = ['toscrape.com/']
  start_urls = ['http://quotes.toscrape.com/']
  # refresh_urls = True # For debug. If efresh_urls = True, start_urls will be crawled again.

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

  # If you need to log in to get the data you want, please rewrite this method
  def login(self):
    html = req.get('http://quotes.toscrape.com/login') # To get csrf_token
    doc = SimplifiedDoc(html)
    csrf_token = doc.getElement('input',attr='name',value='csrf_token').value # get csrf_token
    obj = {'method':'post','url':'http://quotes.toscrape.com/login','data':'csrf_token='+csrf_token+'&username=test&password=test'}
    result = Spider.login(self,obj)
    if result:
      return True
    return False

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ToscrapeSpider())