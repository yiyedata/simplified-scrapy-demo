# simplified-scrapy-demo
simplified-scrapy demo
# Requirements
+ Python 2.7, 3.0+
+ Works on Linux, Windows, Mac OSX, BSD
# run  
```
from simplified_scrapy import SimplifiedMain
SimplifiedMain.startThread()
```
# Demo
Custom crawler class needs to extend Spider class
```
from simplified_scrapy import Spider 
class DemoSpider(Spider):
```
Here is an example of collecting data
```
from simplified_scrapy import Spider, SimplifiedDoc
class DemoSpider(Spider):
  name = 'demo-spider'
  start_urls = ['http://quotes.toscrape.com/']
  allowed_domains = ['quotes.toscrape.com']
  def extract(self, url, html, models, modelNames):
    doc = SimplifiedDoc(html)
    lstA = doc.listA(url=url["url"])
    return [{"Urls": lstA, "Data": None}]

from simplified_scrapy import SimplifiedMain
SimplifiedMain.startThread(DemoSpider())
```

# pip install
simplified-scrapy is backward compatible, and the new version has more functions and faster speed, you can update boldly.
```
pip install -U simplified-scrapy
```
[Examples](https://github.com/yiyedata/simplified-scrapy-demo)

# Legal Issues
In particular, please be aware that

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Translated to human words:

In case your use of the software forms the basis of copyright infringement, or you use the software for any other illegal purposes, the authors cannot take any responsibility for you.

We only ship the code here, and how you are going to use it is left to your own discretion.

