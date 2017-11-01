# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyCrwalerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TtmeijuItem(scrapy.Item):
    title = scrapy.Field()
    urls = scrapy.Field()
    describes = scrapy.Field()

    baiduUrl = scrapy.Field()
    xunleiUrl = scrapy.Field()
    xiaomiUrl = scrapy.Field()
    ed2Url = scrapy.Field()
    btUrl = scrapy.Field()
    kind = scrapy.Field()
    size = scrapy.Field()
    release_time = scrapy.Field()
    subtitle = scrapy.Field()
    chinese_title = scrapy.Field()
    english_title = scrapy.Field()
    season = scrapy.Field()
    episode = scrapy.Field()
    object_id = scrapy.Field()

