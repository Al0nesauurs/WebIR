# -*- coding: utf-8 -*-

BOT_NAME = 'NaBot'

SPIDER_MODULES = ['Na.spiders']
NEWSPIDER_MODULE = 'Na.spiders'

ITEM_PIPELINES = {
  'Na.pipelines.NaPipeline': 300,
}

ROBOTSTXT_OBEY=True
DEPTH_LIMIT = 20