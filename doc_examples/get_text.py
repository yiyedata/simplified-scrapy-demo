#!/usr/bin/python
#coding=utf-8
from simplified_scrapy.spider import SimplifiedDoc 
html='''

<div>
  <div id="1">first text
    <span id="2">span text</span>
    next text
  </div>
</div>
'''
doc = SimplifiedDoc(html) # create doc
div = doc.getElementByID('1')
firstText = div.firstText()
print (firstText) # first text
nextText = div.span.nextText()
print (nextText) # next text
