#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy import SimplifiedDoc
html = '''
<root>
    <item class="class1" id="id1">data1</item>
    <item class="class2" id="id2">>data2</item>
    <item class="class3" id="id3">data3</item>
</root>
'''
doc = SimplifiedDoc(html)
# # Followed by ID, . Followed by class, @ followed by attribute name. If there is a tag, it must be placed first.
item = doc.select('root>#id1')
print(item)
print(item.outerHtml)
assert item.id == 'id1'

# Edit content
item.setContent('test edit')
print(item)
print(item.outerHtml)
assert item.text == 'test edit'

# Edit attribute
item.setAttr(**{"class": "test edit"})
print(item)
print(item.outerHtml)
assert item['class'] == 'test edit'

# Edit attribute
item.setAttrs({"attr1": "attr1", "attr2": "attr2"})
print(item)
print(item.outerHtml)
assert item['attr1'] == 'attr1'

# For properties that do not exist, add
item.setAttr(key="value")
print(item)
print(item.outerHtml)
assert item.key == 'value'

# For value is None, delete
item.setAttr(key=None)
print(item)
print(item.outerHtml)
assert not item.key

assert item.next.id == 'id2'

# Create element
repleace = doc.createElement('replease',
                             'repease data',
                             key='value',
                             id='replease_id')

# Replace itself
item.replaceSelf(repleace)
print(item)
item = doc.select('root>replease')
assert item.outerHtml[:10] == '<replease '
assert item.id == 'replease_id'
assert item.next.id == 'id2'

# Insert before, Insert after
item.insertBefore('<before type="insert">')
item.insertAfter('</before>')
print(item.parent)
assert (item.parent.tag == 'before')

# Remove itself
item.replaceSelf('')
assert not item

# insert child at first
doc.root.insertChild(doc.createElement('insert','insert text'))

# append child
doc.root.appendChild(doc.createElement('append','append text'))

print(doc.html)
