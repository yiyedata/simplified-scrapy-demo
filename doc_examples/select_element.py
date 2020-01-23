#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy.spider import SimplifiedDoc 
html='''
<root>
    <item class="class1" id="id1"><data attr="attr1">data1</data><other>other1</other></item>
    <item class="class2" id="id2"><data attr="attr2">data2</data><other>other2</other></item>
    <item class="class3" id="id3"><data attr="attr3">data3</data><other>other3</other></item>
</root>
'''
doc = SimplifiedDoc(html)
# # Followed by ID, . Followed by class, @ followed by attribute name. If there is a tag, it must be placed first.
print (doc.select('root>#id1'))
print (doc.select('root>@attr=attr1'))
print (doc.select('root>data>text()'))
print (doc.select('root>data>attr()'))
print (doc.selects('root>item>text(data,other)'))

