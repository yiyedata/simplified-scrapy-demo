#!/usr/bin/python
#coding=utf-8
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
title = doc.title # The shorter the path, the better
title = doc.head.title
title = doc.getElementByTag('head').title
title = doc.getElementByText('title')
title = doc.getElementByReg('Example[^>]*title')
print ('-'*50,'title')
print (title) # {'tag': 'title', 'html': 'Example Domain'}
print (title.text) # Example Domain

# Get the first div
div = doc.getElementByTag('div')
div = doc.div # The same as doc.getElementByTag('div'). The shorter the path, the better
div = doc.body.div
div = doc.h1.parent # Position div by h1
print ('-'*50,'first div')
print (div)

# Get the second div
div = doc.getElementByID('test')
div = doc.getElementByClass('demo')
div = doc.getElement('div',attr='class',value='demo')
div = doc.getElementByTag('div',start='</div>') # Use start to locate
div = doc.getElementByTag('div',end='</body>',before='<div') # Use end and before to locate
div = doc.div.next # Position second div by first div
print ('-'*50,'second div')
print (div)
print ('class:',div['class'],'attr:',div.attr,'id:',div.id)
