#!/usr/bin/python
#coding=utf-8
from simplified_scrapy.spider import SimplifiedDoc 
html='''
<!doctype html>
<html>
<head>
  <title>Example Domain</title>
</head>
<body>
  <div class="parent">
    <p class="child">child 11</p>
    <p class="child">child 12</p>
    <p class="child">child 13</p>
  </div>
</body>
</html>
'''
doc = SimplifiedDoc(html) # create doc
div = doc.div
# get children
ps = div.getChildren()
ps = div.children
ps = div.getElementsByTag('p')
ps = div.ps
print ('-'*50,'get children')
print (ps)
# get parent
div = doc.p.getParent()
div = doc.p.getParent(tag="div")
div = doc.p.parent
print ('-'*50,'get parent')
print (div)
# get brothers
p = div.p
p = p.next
print ('next p',p.next)
print ('previous p',p.previous)

