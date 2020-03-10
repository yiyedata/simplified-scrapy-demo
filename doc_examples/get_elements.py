#!/usr/bin/python
#coding=utf-8
# If there is something wrong after running, please update the library. pip install -U simplified_scrapy
from simplified_scrapy.spider import SimplifiedDoc 
html='''
<table>
  <tbody>
    <tr>
      <th class="ch">index</th>
      <th class="ch">title</th>
    </tr>
    <tr>
      <td class="cd">1</td>
      <td class="cd">title 1</td>
    </tr>
    <tr>
      <td class="cd">2</td>
      <td class="cd">title 2</td>
    </tr>
    <tr>
      <td class="cd">3</td>
      <td class="cd">title 3</td>
    </tr>
  </tbody>
</table>
'''
doc = SimplifiedDoc(html) # create doc
# get all rows
rows = doc.getElementsByTag('tr')
assert len(rows)==4
rows = doc.trs
assert len(rows)==4
rows = doc.tbody.getChildren()
assert len(rows)==4
rows = doc.tbody.children
assert len(rows)==4
rows = doc.selects('tr')
assert len(rows)==4
print ('-'*50,'get all rows')
print (rows)
# get rows except header
rows = doc.getElementsByReg('<td.*>')
assert len(rows)==3
print ('-'*50,'get all rows except header')
print (rows)

print ('-'*30,'get all cells')
# get all cells, td and th
for row in rows:
  cels = row.getElementsByTag(['th','td'])
  cels = row.children
  print (cels)
  cels = row.selects('th|td>text()')
  print (cels)
# get all cells. You can use select, selects, getElement and other methods for list data
cels = rows.selects('th|td>text()')
assert cels[2][0]=='3'
# print (cels)

table = doc.getTable()
assert table[3][0]=='3'

# Filter out the header
rows = doc.trs.notContains('<th')
assert len(rows)==3
rows = doc.trs.contains('<td')
assert len(rows)==3
rows = doc.getElementsByTag('tr',start='</tr>')
assert len(rows)==3
rows = doc.tr.getNexts()
assert len(rows)==3
rows = doc.tr.nexts
assert len(rows)==3
print ('-'*50,'Get all rows except header')
print (rows)
print (rows[0].getText(','))
