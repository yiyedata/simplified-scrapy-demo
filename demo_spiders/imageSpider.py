#!/usr/bin/python
#coding=utf-8
import os,io,sys
from simplified_scrapy.core.spider import Spider 
class ImageSpider(Spider):
  # concurrencyPer1s=2
  name = 'demo-image-spider'
  # models = ['auto_main']
  start_urls = ['http://www.umei.cc/touxiangtupian/3.htm']

  def __init__(self):
    Spider.__init__(self,self.name) #necessary
    if(not os.path.exists('images/')):
      os.mkdir('images/')
    self.url_store.resetUrls(self.start_urls)

  def afterResponse(self, response, url):
    try:
      if sys.version_info.major == 2:
        maintype = response.headers.maintype
      else: maintype =response.info().get('Content-Type')
      if(response.code==200 and maintype and maintype.find('image')>=0):
        name = 'images'+url[url.rindex('/'):]
        file = io.open(name, "ab")
        file.write(response.read())
        file.close()
        return None
      else:
        html = Spider.afterResponse(self, response, url)
        return Spider.removeScripts(self, html)
    except Exception as err:
      print (err)

  def extract(self, url,html,models,modelNames):
    urls = self.listImg(html)
    if(urls and len(urls)):
      self.saveUrl(urls)
    return Spider.extract(self, url,html,models,modelNames)

  def urlFilter(self,url):
    if(not self.isPageUrl(url)):
      #采集后缀为jpeg.jpg.png.gif的图片
      if("jpeg.jpg.png.gif".find(url[-4:].lower())<0):
        return False
    return True