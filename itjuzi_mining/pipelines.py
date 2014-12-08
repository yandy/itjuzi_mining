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
        company = session.query(Company).filter(Company.name == item['name']).first()
        if company:
          company.url = item['url']
          company.date = item['date']
          company.location = item['location']
          company.state = item['state']
          company.stage = item['stage']
          company.area = item['area']
          company.tags = item['tags']
          company.desc = item['discr']
        else:
          company = Company(**item)
          session.add(company)
        session.commit()
      elif spider.name == 'investevents':
        pass
      return item
