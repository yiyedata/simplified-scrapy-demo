
import hashlib
from simplified_scrapy.core.mongo_urlstore import MongoUrlStore
class MeishiUrlStore(MongoUrlStore):
  def checkUrl(self,url,i):
    db = self._connect()
    id = hashlib.md5(url).hexdigest()
    tbName = self._tbName
    url = db[tbName].find_one({"_id": id})
    if(not url and i):
      tbName = tbName+str(i)
      url = db[tbName].find_one({"_id": id})
    return url