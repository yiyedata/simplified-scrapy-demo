#!/usr/bin/python
#coding=utf-8
import os,io,sys
from simplified_scrapy.spider import Spider, SimplifiedDoc
class ImageSpider(Spider):
  name = 'pexels.com'
  start_urls = ['https://www.pexels.com/']

  def __init__(self):
    Spider.__init__(self,self.name) #necessary
    if(not os.path.exists('images/')):
      os.mkdir('images/')

  def afterResponse(self, response, url, error=None):
    try:
      if sys.version_info.major == 2: maintype = response.headers.maintype
      else: maintype =response.info().get('Content-Type')
      # save image
      if(response.code==200 and maintype and maintype.find('image')>=0):
        name = 'images'+url[url.rindex('/'):]
        index = name.find('?')
        if index>0: name = name[:index]
        file = io.open(name, "wb")
        file.write(response.read())
        file.close()
        return None
      else: # If it's not a image, leave it to the frame
        return Spider.afterResponse(self, response, url, error)
    except Exception as err:
      print (err)

  def extract(self,url,html,models,modelNames):
    urls = SimplifiedDoc(html).listImg(url=url['url'])
    if(urls):
      self.saveUrl(urls)
    return True

  def urlFilter(self,url):
    # Suffix filter
    if(".svg".find(url[-4:].lower())>0):
      return False
    return True

from simplified_scrapy.simplified_main import SimplifiedMain
SimplifiedMain.startThread(ImageSpider())