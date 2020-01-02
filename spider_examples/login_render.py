from simplified_scrapy.spider import Spider, SimplifiedDoc
from simplified_html.request_render import RequestRender
class RequestRenderEx(RequestRender):
  async def afterGoto(self,page,js):
    await page.evaluate(
          '''() =>{Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.type("#username", "demo")
    await page.type("#password", "123456")
    await page.waitFor(100)
    await page.evaluate('''document.getElementsByClassName("btn btn-primary")[0].click()''') 
    await page.waitFor(1000)

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

  req = RequestRenderEx({ 'executablePath': '/Applications/chrome.app/Contents/MacOS/Google Chrome'})
  # If you need to log in to get the data you want, please rewrite this method
  def login(self):
    self.req.getCookies('http://quotes.toscrape.com/login', self._callback) # To get csrf_token
    return True
  def _callback(self,cookie,url,data):
    if cookie:
      self.setCookie(url,cookie)
    else:
      self.logged_in = False # If the login is not successful, try again next time

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ToscrapeSpider())