"""
例子：需要登录才能访问的数据采集方法
"""
import json
from simplified_scrapy.core.spider import Spider 
class LoginDemoSpider(Spider):
  name = 'demo-login-spider'
  start_urls = [{'url':'http://47.92.87.212:8080/yiye.mgt/api/push/list',
    'requestMethod':'post',
    'postData':'{"index":1,"tbName":"biaoshu","keyword":"","count":10}'}]

  def afterResponse(self, response, url):
    if(response.code==403):
      print 'login result:' + str(self.login())
      return None
    html = Spider.afterResponse(self, response, url)
    return Spider.removeScripts(self, html)

  def login(self):
    login_data={
      'url':'http://47.92.87.212:8080/yiye.mgt/api/pub/login',
      'headers': { 'User-Agent' : 'yazz', "Content-Type": "application/json",
        "Referer":"http://47.92.87.212:8080/yiye.mgt/view/login.jsp"
      },
      'data': {'name':'demo', 'pwd':'123456','url':'123'}
    }
    html = Spider.login(self,login_data)
    if(html):
      obj = json.loads(html)
      return obj.get('code')==1
    return False

# test=LoginDemoSpider()
# test.login()
