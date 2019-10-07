# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from mp3download.items import Mp3DownloadItem


class Mp3scraperSpider(scrapy.Spider):
    name = 'mp3scraper'
    allowed_domains = ['naasongs.com']
    start_urls = ['https://naasongs.com/telugu-songs-b/']

    def parse(self, response):
        for href in response.css('.home-devotional a::attr(href)').getall():
            yield response.follow(href, self.parse_album)
    
    def parse_album(self, response):
        l = ItemLoader(item = Mp3DownloadItem(),response= response)
        l.add_css('album','.breadcrumb_last::text' )
        l.add_css('url', 'blockquote a::attr(href)')
        return l.load_item()

        
