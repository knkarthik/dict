# -*- coding: utf-8 -*-
import scrapy


class DictSpiderSpider(scrapy.Spider):
    name = 'dict_spider'
    allowed_domains = ['https://www.mso.anu.edu.au/~ralph/OPTED/',  'www.mso.anu.edu.au']
    start_urls = ['http://www.mso.anu.edu.au/~ralph/OPTED/v003/']
    words_dict = {}

    def parse(self, response):
        links = response.xpath("//a[contains(@href, 'wb1913')]")
        
        for link in links:
            linkToGet = link.css('a::attr(href)').get()
            print("***LINK TO GET**", linkToGet)
            yield response.follow(linkToGet, self.parse_links)
        
    def parse_links(self, response):
        words = response.xpath("//p/b/text()")
        for word in words:
            yield {
                f'{word.extract()}': 1
                }
        
        


