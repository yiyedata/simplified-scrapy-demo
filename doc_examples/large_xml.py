from simplified_scrapy import SimplifiedDoc, utils, req

doc = SimplifiedDoc()
# Load the file line by line.
doc.loadFile('doc_examples/large.xml', lineByline=True)
# Get iterator
for user in doc.getIterable(tag='User'):
  print (user.children.text)

assert user.children.text[0]=='Sven'