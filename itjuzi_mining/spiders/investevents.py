import scrapy, cPickle

from itjuzi_mining.items import InvesteventItem
from itjuzi_mining.settings import REGEXS
from scrapy.contrib.linkextractors import LinkExtractor

class InvesteventsSpider(scrapy.Spider):
  name = "investevents"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/investevents']
  link_extractor = LinkExtractor(allow=REGEXS['investevents_crawl_url'])

  def parse(self, response):
    for sel in response.xpath("//table[@class='children-norml-link']//tbody//tr"):
      url = ''.join(sel.xpath("td[1]/span[@class='invse_id']/text()").extract())
      matched = REGEXS['investevents_item_url'].search(url)
      if matched:
        item = InvesteventItem()
        item['itid'] = int(matched.group('itid'))
        item['date'] = ''.join(sel.xpath('td[1]/text()').extract())
        item['company'] = ''.join(sel.xpath('td[2]/a/text()').extract())
        item['turn'] = ''.join(sel.xpath('td[3]/a/text()').extract())
        item['money'] = ''.join(sel.xpath('td[4]/text()').extract())
        item['area'] = ''.join(sel.xpath('td[5]/a/text()').extract())
        item['investfirms'] = sel.xpath('td[6]/a/text()').extract()
        yield item
    for link in self.link_extractor.extract_links(response):
      yield scrapy.Request(url=link.url, callback=self.parse)
