#!/usr/bin/python
#coding=utf-8
from simplified_scrapy import SimplifiedDoc 
html='''
<root>
  <list id="1">
    <name id="2"><strong>name 1</strong></name>
    <name id="3">name 2</name>
    <name id="4">name 3</name>
  </list>
</root>
'''
doc = SimplifiedDoc(html) # create doc
ele = doc.select('name#2') # doc.getElementByID('2',tag='name')
assert ele.id=='2'
# Each object obtained by doc and the object obtained by this object have the following properties, 
# except for the object with an empty value.
# The object in the example also has an id attribute
print('id = {}\ntag = {}\nhtml = {}\ntext = {}\nouterHtml = {}\n_start = {}\n_end = {}'.format(
  ele.id, ele.tag, ele.html, ele.text, ele.outerHtml, ele._start, ele._end))
# _start and _end represent the start and end position of the object label in html.
flag = ele.outerHtml == doc.html[ele._start:ele._end]
assert flag
assert ele.outerHtml[:len('<name id="2">')] == '<name id="2">'
