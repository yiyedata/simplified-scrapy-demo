import requests
from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_html.request_render import RequestRender
class ToscrapeSpider(Spider):
  name = 'toscrape.com'
  allowed_domains = ['toscrape.com/']
  start_urls = [{'url':'http://quotes.toscrape.com/','requestMethod':'render'}] # Set requestMethod = render 
  # refresh_urls = True # For debug. If efresh_urls = True, start_urls will be crawled again.
  
  req = RequestRender({ 'executablePath': '/Applications/chrome.app/Contents/MacOS/Google Chrome'})
  def renderUrl(self,url,callback):
    self.req.get(url['url'],self._callback,extr_data=(url,callback)) # Use requests to download the page and return the HTML string

  def _callback(self,html,url,extr_data):
    extr_data[1](html,extr_data[0],self)

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
    if nextA:
      for a in nextA:
        a['requestMethod']='render' # Set download method 
    return {"Urls": nextA, "Data": data}

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ToscrapeSpider())