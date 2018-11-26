# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeSpliderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #汽车的品牌
    car_name = scrapy.Field()
    #汽车的报价
    car_quota = scrapy.Field()
    #汽车的图库
    car_pictures = scrapy.Field()
    #汽车的论坛
    car_bbs = scrapy.Field()
    pass
