from spider_resource import proxyips
from simplified_scrapy.simplified_doc import SimplifiedDoc 
from simplified_scrapy.request import req
html = req.get('https://free-proxy-list.net')
doc = SimplifiedDoc(html)
table = doc.getElementByID('proxylisttable')
trs = table.tbody.trs
ips = {'https':[],'http':[]}
for tr in trs:
  tds = tr.tds
  if tds[6].text == 'yes':
    ips['https'].append({'ip':'https://'+tds[0].text+':'+tds[1].text})
  else:
    ips['http'].append({'ip':'http://'+tds[0].text+':'+tds[1].text})

proxyips['http'].clear()
proxyips['http'].extend(ips['http'])
proxyips['https'].clear()
proxyips['https'].extend(ips['https'])
