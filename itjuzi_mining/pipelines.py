# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from . import Session
from models import Company, Investevent
from items import CompanyItem, InvesteventItem
from settings import URL_REGEXS

class ItjuziMiningPipeline(object):
    def process_item(self, item, spider):
      session = Session()
      if isinstance(item, CompanyItem):
        it = item.copy()
        company = Company(**it)
        session.merge(company)
        session.commit()
      elif isinstance(item, InvesteventItem):
        it = item.copy()
        company = it.pop('company')
        matched = URL_REGEXS['companies_item_url'].search(company)
        if matched:
          it['company_id'] = int(matched.group('itid'))
        investfirms = it.pop('investfirms')
        it['investfirms'] = []
        for ifirm in investfirms:
          matched = URL_REGEXS['investevents_item_url'].search(ifirm)
          if matched:
            itid = int(matched.group('itid'))
            investfirm = session.query(Investfirm).filter(Investfirm.itid == itid).first()
            if investfirm is None:
              investfirm = Investfirm(itid=itid)
            it['investfirms'].append(investfirm)
        investevent = Investevent(**it)
        session.merge(investevent)
        session.commit()
      return item
