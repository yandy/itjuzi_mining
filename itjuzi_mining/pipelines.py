# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from . import Session
from models import Company

class ItjuziMiningPipeline(object):
    def process_item(self, item, spider):
      session = Session()
      if spider.name == 'companies':
        company = Company(**item)
        session.merge(company)
        session.commit()
      elif spider.name == 'investevents':
        investevent = Investevent(**item)
        session.merge(investevent)
        session.commit()
      return item
