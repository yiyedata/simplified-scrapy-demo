#!/usr/bin/python
#coding=utf-8
"""
下载小说的例子
"""
import io,json
from simplified_scrapy.core.spider import Spider 
from simplified_scrapy.core.utils import getTimeNow,printInfo,appendFile

class TianshuSpider(Spider):
  concurrencyPer1s=1
  name = 'tianshu-spider'
  start_urls = []
  def __init__(self):
    i=1
    while(i<=33):
      self.start_urls.append('https://m.biqudao.cc/0/779_{}/'.format(i))
      i+=1
    Spider.__init__(self,self.name) #necessary

  def sortBy(self, obj):
    return obj["url"]
  def extract(self, url, html, models, modelNames):
    try:
      html = self.removeScripts(html)
      lst=[]
      data=[]
      ele = None
      if(url["url"].find('https://m.biqudao.cc/0/779_')==0):
        # pass
        lstA = self.listA(html,url["url"])
        for a in lstA:
          if(a["url"].find('https://m.biqudao.cc/book/779/') == 0):
            lst.append(a)
        # lst.sort(key=self.sortBy,reverse=False)
      elif(url["url"].find('https://m.biqudao.cc/book/779/')==0):
        ele = self.getElementByID("chaptertitle",html)
        if(ele):
          title = ele["innerText"]
          ele = self.getElementByID("novelcontent",html)
          if(ele):
            content = ele["innerText"]
            data.append({"Title": title, "Content": content})
            nextPage = self.getElementByID('pb_next',html)
            if(nextPage): 
              lst.append({"url":"https://m.biqudao.cc"+nextPage["href"],"title":title})

      return [{"Urls": lst, "Data": data}]
    except Exception as e:
      printInfo(e)
    
  def __getitem__(self, k):
    return self[k]
  def afterResponse(self, response, url):
    html = Spider.afterResponse(self, response, url)
    return Spider.removeScripts(self, html)


def sortBy(obj):
  title = obj["Title"]
  i = title.find('.')
  if(i<0): 
    i=3
  num = title[0:i]
  return int(num)
def sortFile():
  import sys
  if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
  name = 'tianshu-spider'
  src = 'data/{}_obj.json'.format(name)
  dest = 'data/{}_obj_dest.json'.format(name)
  srcfile = io.open(src, "r",encoding="utf-8")
  lines = srcfile.readlines()
  lst=[]
  for line in lines:
    lst.append(json.loads(line))
  lst.sort(key=sortBy,reverse=False)
  for l in lst:
    appendFile(dest,
    l["Content"]
      .replace('笔趣岛 m.biqudao.cc  一秒记住【笔趣岛 www.biqudao.cc】，无弹窗，更新快，免费阅读！','\n')
      .replace('笔趣岛 m.biqudao.cc','\n'))

sortFile()