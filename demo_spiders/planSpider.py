"""
二级域名采集，自动抽取文章数据，配置定时更新
"""
from simplified_scrapy.core.spider import Spider

class PlanSpider(Spider):
  name = 'plan-spider'
  start_urls = ['http://www.scrapyd.cn/']
  models = ['auto_main','auto_obj']

  def afterResponse(self, response, url):
    html = Spider.afterResponse(self, response, url)
    return Spider.removeScripts(self, html)

  #如果需要定期采集，可以实现plan方法
  def plan(self):
    return [{'hour':10,'minute':30},{'hour':16,'minute':0}]
