#!/usr/bin/python
#coding=utf-8
from simplified_scrapy.spider import SimplifiedDoc 
html='''

<root>
  <names id="1">
    <name id="2">name 1</name>
    <name id="3">name 2</name>
    <name id="4">name 3</name>
  </names>
</root>
'''
doc = SimplifiedDoc(html) # create doc
# If the name ends in s
ele = doc.names
# The same as 
ele = doc.select('names') if doc.select('names') else doc.selects('name')
# So if you want to get list data
names = doc.names.names
print(names)
# Of course, you can get it in other ways
names = doc.selects('name')
names = doc.getElementsByTag('name')