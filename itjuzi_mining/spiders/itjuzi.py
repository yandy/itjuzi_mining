import scrapy, cPickle, re

from itjuzi_mining.items import CompanyItem
from itjuzi_mining.settings import URL_REGEXS
from scrapy.contrib.linkextractors import LinkExtractor

URL_REGEX = re.compile('|'.join(URL_REGEXS.values()))

class ItjuziSpider(scrapy.Spider):
  name = "itjuzi"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/company', 'http://itjuzi.com/investevents']
  link_extractor = LinkExtractor(allow=URL_REGEX)

  def parse(self, response):
    for link in self.link_extractor.extract_links(response):
      yield scrapy.Request(url=link.url, callback=self.parse)

    matched = URL_REGEX.search(response.url)
    if matched is None:
      return
    elif matched.group('cid'):
      self._parse_company(response, id=matched.group('cid'))
    elif matched.group('ieid'):
      self._parse_investevents(response, id=matched.group('ieid'))

  def _parse_company(self, response, id):
    for sel in response.xpath("//ul[@class='detail-info']"):
      item = CompanyItem()
      item['itid'] = int(id)
      item['name'] = ''.join(sel.xpath('li[2]/em/text()').extract())
      item['url'] = ''.join(sel.xpath('li[1]/a/@href').extract())
      item['date'] = ''.join(sel.xpath('li[3]/em/text()').extract())
      item['location'] = ''.join(sel.xpath('li[4]/a/text()').extract())
      item['state'] = ''.join(sel.xpath('li[5]/a/text()').extract())
      item['stage'] = ''.join(sel.xpath('li[6]/a/text()').extract())
      item['area'] = ''.join(sel.xpath('li[7]/a/text()').extract())
      item['tags'] = cPickle.dumps(sel.xpath('li[8]/a/text()').extract())
      item['discr'] = ''.join(sel.xpath('li[9]/em/text()').extract())
      item['investevents'] = []
      item['mergeevent'] = None
      yield item

  def _parse_investevents(self, response, id):
    for sel in response.xpath("//table[@id='company-member-list']//tbody"):
      item = InvesteventItem()
      item['itid'] = int(id)
      item['date'] = ''.join(sel.xpath('tr[1]/td[2]/text()').extract())
      item['company'] = ''.join(sel.xpath('tr[2]/td[2]/a/@href').extract())
      item['area'] = ''.join(sel.xpath('tr[3]/td[2]/a/text()').extract())
      item['money'] = ''.join(sel.xpath('tr[4]/td[2]/text()').extract())
      item['turn'] = ''.join(sel.xpath('tr[5]/td[2]/a/text()').extract())
      item['investfirms'] = sel.xpath('tr[6]/td[2]/a/@href').extract()
      yield item
