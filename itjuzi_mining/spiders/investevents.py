import scrapy
import cPickle

from itjuzi_mining.items import InvesteventItem

class InvesteventsSpider(scrapy.Spider):
  name = "investevents"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/investevents?page=%s' % page for page in xrange(1,603)]

  def parse(self, response):
    for sel in response.xpath("//table[@class='children-norml-link']//tbody//tr"):
      item = InvesteventItem()
      item['date'] = ''.join(sel.xpath('td[1]/text()').extract())
      item['company'] = ''.join(sel.xpath('td[2]/a/text()').extract())
      item['turn'] = ''.join(sel.xpath('td[3]/a/text()').extract())
      item['money'] = ''.join(sel.xpath('td[4]/text()').extract())
      item['area'] = ''.join(sel.xpath('td[5]/a/text()').extract())
      item['investor'] = sel.xpath('td[6]/a/text()').extract()
      yield item
