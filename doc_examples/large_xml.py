from simplified_scrapy import SimplifiedDoc, utils, req

doc = SimplifiedDoc()
# Load the file line by line.
doc.loadFile('doc_examples/large.xml', lineByline=True)
# Get iterator
for d in doc.getIterable(tag='User'):
  print (d.User.children.text)

assert d.User.children.text[0]=='Sven'
