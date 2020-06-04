# -*- coding: utf-8 -*-


from ..items import HomepageItem
import scrapy


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains = ['news.ycombinator.com']

    def start_requests(self):
        return [scrapy.Request("https://news.ycombinator.com/news", meta={'proxy': self.settings.get('PROXY')})]

    def parse(self, response):
        itemlists = response.xpath('//table[@class="itemlist"]/tr')
        for i in range(0, len(itemlists) - 2, 3):
            item = HomepageItem()
            content = itemlists[i]
            subtext = itemlists[i + 1]
            item['title'] = content.xpath('./td[@class="title"]/a/text()').get()
            item['source_website'] = content.xpath('./td[@class="title"]/span/a/span/text()').get()
            item['points'] = subtext.xpath('./td[@class="subtext"]/span/text()').get()
            item['comments'] = subtext.xpath('./td[@class="subtext"]/a/text()').getall()[-1]
            item['source'] = 'hackernews_homepage'
            yield item
