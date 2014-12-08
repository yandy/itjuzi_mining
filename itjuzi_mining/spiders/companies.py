import scrapy, re, cPickle

from itjuzi_mining.items import CompanyItem
from itjuzi_mining.settings import REGEXS
from scrapy.contrib.linkextractors import LinkExtractor

class CompaniesSpider(scrapy.Spider):
  name = "companies"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/company']
  link_extractor = LinkExtractor(allow=REGEXS['companies_crawl_url'])

  def parse(self, response):
    if REGEXS['companies_item_url'].search(response.url):
      for sel in response.xpath("//ul[@class='detail-info']"):
        item = CompanyItem()
        item['name'] = ''.join(sel.xpath('li[2]/em/text()').extract())
        item['url'] = ''.join(sel.xpath('li[1]/a/text()').extract())
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
    else:
      for link in self.link_extractor.extract_links(response):
        yield scrapy.Request(url=link.url, callback=self.parse)
