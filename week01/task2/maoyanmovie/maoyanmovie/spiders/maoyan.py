# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        details = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for i in range(10):
            detail = details[i]
            item = MaoyanmovieItem()
            title = detail.xpath('./div[1]/span[1]/text()').extract()[0]
            movie_type = detail.xpath('./div[2]/text()[2]').extract()[0].strip()
            release_date = detail.xpath('./div[4]/text()[2]').extract()[0].strip()
            item['title'] = title
            item['movie_type'] = movie_type
            item['release_date'] = release_date
            yield item
