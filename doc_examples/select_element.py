#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy import SimplifiedDoc 
html='''
<root>
    <item class="class1" id="id1"><data attr="attr1">data1</data><other>other1</other></item>
    <item class="class2" id="id2"><data attr="attr2">data2</data><other>other2</other></item>
    <item class="class3" id="id3"><data attr="attr3">data3</data><other>other3</other></item>
</root>
'''
doc = SimplifiedDoc(html)
# # Followed by ID, . Followed by class, @ followed by attribute name. If there is a tag, it must be placed first.
item = doc.select('root>#id1')
assert item.id=='id1'
print (item)
# The same as 
item = doc.getElementByTag('root').getElementByID('id1')
assert item.id=='id1'
print (item)
item = doc.select('root>@attr=attr1')
assert item.attr=='attr1'
print (item)
item = doc.select('root>data>text()')
assert item=='data1'

item = doc.select('root>data>attr()')
assert item=='attr1'

assert 'attr1'==doc.getElementByTag('root').getElementByTag('data').attr
print (doc.selects('root>item>text(other),data>attr()'))
assert 'attr3'==doc.selects('root>item>text(other),data>attr()')[2][1]
print (doc.selects('root>item>text(other,data),data>attr()'))
assert 'attr3'==doc.selects('root>item>text(other,data),data>attr()')[2][2]

print (doc.selects('root>item>(data>attr())'))
assert 'attr3'==doc.selects('root>item>(data>attr())')[2]
# The same as 
print ([item.select('data>attr()') for item in doc.getElementByTag('root').getElementsByTag('item')])
print (doc.selects('root>item>data>attr()'))
# The same as 
print ([item.attr for item in doc.getElementByTag('root').getElementByTag('item').getElementsByTag('data')])

