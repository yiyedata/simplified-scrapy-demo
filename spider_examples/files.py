#!/usr/bin/python
#coding=utf-8
import os
from simplified_scrapy import Spider, SimplifiedDoc, utils, SimplifiedMain


class ImageSpider(Spider):
    name = 'pexels.com'
    start_urls = ['https://www.pexels.com/']

    # refresh_urls = True
    imgPath = 'images/'
    def __init__(self):
        Spider.__init__(self, self.name)  #necessary
        if (not os.path.exists(self.imgPath)):
            os.mkdir(self.imgPath)

    def afterResponse(self, response, url, error=None, extra=None):
        try:
            utils.saveResponseAsFile(response, self.imgPath, 'image')
        except Exception as err:
            print(err)
        return None

    def extract(self, url, html, models, modelNames):
        urls = SimplifiedDoc(html).listImg(url=url['url'])
        if (urls):
            self.saveUrl(urls)
        return True

    def urlFilter(self, url):
        # Suffix filter
        if (".svg".find(url[-4:].lower()) > 0):
            return False
        return True


SimplifiedMain.startThread(ImageSpider())
