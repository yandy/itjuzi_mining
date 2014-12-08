# -*- coding: utf-8 -*-

# Scrapy settings for itjuzi_mining project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import re

BOT_NAME = 'itjuzi_mining'

SPIDER_MODULES = ['itjuzi_mining.spiders']
NEWSPIDER_MODULE = 'itjuzi_mining.spiders'

ITEM_PIPELINES = { 'itjuzi_mining.pipelines.ItjuziMiningPipeline': 1 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'itjuzi_mining (+http://www.yourdomain.com)'

DATABASE = {
  'drivername': 'sqlite',
  'database': 'itjuzi'
}

REGEXS = {
  'companies_crawl_url': re.compile('^http://itjuzi\.com/company\?page=\d+|http://itjuzi\.com/company/\d+'),
  'companies_item_url': re.compile('^http://itjuzi\.com/company/\d+')
}
