# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InvesteventItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  itid = scrapy.Field()
  date = scrapy.Field()
  money = scrapy.Field()
  area = scrapy.Field()
  turn = scrapy.Field()
  company = scrapy.Field()
  investfirms = scrapy.Field()

  ITEM_NAME = 'investevent'

class CompanyItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  itid = scrapy.Field()
  name = scrapy.Field()
  url = scrapy.Field()
  date = scrapy.Field()
  location = scrapy.Field()
  state = scrapy.Field()
  area = scrapy.Field()
  stage = scrapy.Field()
  tags = scrapy.Field()
  discr = scrapy.Field()
  investevents = scrapy.Field()
  mergeevent = scrapy.Field()

  ITEM_NAME = 'company'
