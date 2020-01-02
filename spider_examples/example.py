from simplified_scrapy.spider import Spider, SimplifiedDoc
class MySpider(Spider):
  name = 'example.com'
  allowed_domains = ['example.com']
  start_urls = [
    'http://www.example.com/',
    'http://www.example.com/1.html',
    'http://www.example.com/2.html',
    'http://www.example.com/3.html',
  ]
  # refresh_urls = True # For debug. If efresh_urls = True, start_urls will be crawled again.
  
  def extract(self, url, html, models, modelNames):
    doc = SimplifiedDoc(html)
    lstA = doc.listA(url=url["url"]) # Get link data for subsequent crawling
    data = [{"title":doc.title.text}] # Get target data
    return {"Urls": lstA, "Data": data} # Return data to framework

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(MySpider()) # Start crawling