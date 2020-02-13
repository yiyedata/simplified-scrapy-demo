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
assert firstText=='first text'
print (firstText) # first text
nextText = div.span.nextText()
assert nextText=='next text'
print (nextText) # next text
previousText = div.span.previousText()
assert previousText=='first text'
print (previousText) # first text