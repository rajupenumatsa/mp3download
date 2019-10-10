# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp3DownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    album_title = scrapy.Field()
    cast = scrapy.Field()
    music = scrapy.Field()
    track_count = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

