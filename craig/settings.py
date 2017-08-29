# -*- coding: utf-8 -*-

BOT_NAME = 'craig'

SPIDER_MODULES = ['craig.spiders']
NEWSPIDER_MODULE = 'craig.spiders'

ITEM_PIPELINES = {
  'craig.pipelines.CraigPipeline': 300,
}

ROBOTSTXT_OBEY=True
