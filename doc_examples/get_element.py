#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy.spider import SimplifiedDoc 
html='''
<!doctype html>
<html>
<head>
    <title>Example Domain title</title>
    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
<div class='demo' attr='test' id='test'>
    <h1>2 Example Domain</h1>
    <p>2 This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">2 More information...</a></p>
</div>
</body>
</html>
'''
doc = SimplifiedDoc(html) # create doc
# The way to get title is as follows
title = doc.getElementByTag('title')
assert title.text == 'Example Domain title'
title = doc.title # The shorter the path, the better
assert title.text == 'Example Domain title'
title = doc.head.title
assert title.text == 'Example Domain title'
title = doc.getElementByTag('head').title
assert title.text == 'Example Domain title'
title = doc.getElementByText('title')
assert title.text == 'Example Domain title'
title = doc.getElementByReg('Example[^>]*title')
assert title.text == 'Example Domain title'
print ('-'*50,'title')
print (title) # {'tag': 'title', 'html': 'Example Domain'}
print (title.text) # Example Domain

# Get the first div
div = doc.getElementByTag('div')
assert div.h1.text == 'Example Domain'
div = doc.div # The same as doc.getElementByTag('div'). The shorter the path, the better
assert div.h1.text == 'Example Domain'
div = doc.body.div
assert div.h1.text == 'Example Domain'
div = doc.h1.parent # Position div by h1
assert div.h1.text == 'Example Domain'
print ('-'*50,'first div')
print (div)

# Get the second div
div = doc.getElementByID('test')
assert div.id == 'test'
div = doc.getElementByClass('demo')
assert div.id == 'test'
div = doc.getElement('div',attr='class',value='demo')
assert div.id == 'test'
div = doc.getElementByTag('div',start='</div>') # Use start to locate
assert div.id == 'test'
div = doc.getElementByTag('div',end='</body>',before='<div') # Use end and before to locate
assert div.id == 'test'
div = doc.div.next # Position second div by first div
assert div.id == 'test'
print ('-'*50,'second div')
print (div)
print ('class:',div['class'],'attr:',div.attr,'id:',div.id)

# use select geting the second div
div = doc.select('#test')
assert div.id == 'test'
div = doc.select('div#test')
assert div.id == 'test'
div = doc.select('div.demo')
assert div.id == 'test'
div = doc.select('div@attr=test')
assert div.id == 'test'
print ('-'*50,'second div')
print (div)
# use select geting the second h1 
# # Followed by ID, . Followed by class, @ followed by attribute name. If there is a tag, it must be placed first.
h1 = doc.select('#test>h1')
assert h1.text == '2 Example Domain'
h1 = doc.select('div#test>h1')
assert h1.text == '2 Example Domain'
h1 = doc.select('div.demo>h1')
assert h1.text == '2 Example Domain'
h1 = doc.select('div@attr=test>h1')
assert h1.text == '2 Example Domain'
print ('-'*50,'second h1')
print (h1)
# use text() get the text
h1 = doc.select('div#test>h1>text()')
assert h1 == '2 Example Domain'


