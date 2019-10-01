# -*- coding: utf-8 -*-
import scrapy


class Mp3scraperSpider(scrapy.Spider):
    name = 'mp3scraper'
    allowed_domains = ['naasongs.com']
    start_urls = ['https://naasongs.com/telugu-songs-b/']

    def parse(self, response):
        for href in response.css('.home-devotional a::attr(href)').getall():
            yield response.follow(href, self.parse_album)
    
    def parse_album(self, response):
        yield{
            'album' : response.css('.breadcrumb_last::text').get(default = 'null').strip(),
            'link' : response.css('blockquote a::attr(href)').get(default = 'null').strip(),
        }
