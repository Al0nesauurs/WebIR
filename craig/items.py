# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_from = scrapy.Field()
    # The destination URL
    html = scrapy.Field()
    url = scrapy.Field()
    url_to = scrapy.Field()

    count = scrapy.Field()