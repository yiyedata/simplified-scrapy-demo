#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy import SimplifiedDoc 
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
assert div['class']=='parent'
# get children
ps = div.getChildren()
assert len(ps)==3
ps = div.children
assert len(ps)==3
ps = div.getElementsByTag('p')
assert len(ps)==3
ps = div.ps
assert len(ps)==3
print ('-'*50,'get children')
print (ps)
# get parent
div = doc.p.getParent()
assert div['class']=='parent'
div = doc.p.getParent(tag="div")
assert div['class']=='parent'
div = doc.p.parent
assert div['class']=='parent'
print ('-'*50,'get parent')
print (div)
# get brothers
p = div.p
assert p.text=='child 11'
p = p.next
assert p.text=='child 12'
p = p.next
assert p.text=='child 13'
assert not p.next
ps = p.previous
assert len(ps)==2
print ('previous p',ps)

