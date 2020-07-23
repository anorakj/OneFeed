# -*- coding: utf-8 -*-


from ..items import HomepageItem
import scrapy


class HomepageSpider(scrapy.Spider):
    name = 'hackernews homepage'
    allowed_domains = ['news.ycombinator.com']

    def start_requests(self):
        meta = {'proxy': self.settings.get('PROXY')} if self.settings.get('PROXY') else None
        return [scrapy.Request("https://news.ycombinator.com/news", meta=meta)]

    def parse(self, response):
        itemlists = response.xpath('//table[@class="itemlist"]/tr')
        for i in range(0, len(itemlists) - 2, 3):
            item = HomepageItem()
            content = itemlists[i]
            subtext = itemlists[i + 1]
            item['title'] = content.xpath('./td[@class="title"]/a/text()').get()
            item['link'] = content.xpath('./td[@class="title"]/a/@href').get()
            item['points'] = subtext.xpath('./td[@class="subtext"]/span/text()').get()
            item['comments'] = subtext.xpath('./td[@class="subtext"]/a/text()').getall()[-1]
            item['source'] = 'hackernews_homepage'
            yield item
