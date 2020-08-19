# -*- coding: utf-8 -*-
import json
import time

from ..items import ArticlesItem
import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'infoq_articles'
    allowed_domains = ['www.infoq.cn']
    headers = {'origin': 'https://www.infoq.cn', 'referer': 'https://www.infoq.cn', 'host': 'www.infoq.cn'}

    def start_requests(self):
        self.request_index = 0
        return [scrapy.Request("https://www.infoq.cn/public/v1/my/recommond", headers=self.headers, method='POST',
                               body=json.dumps({'size': 12, 'score': int(1e3 * (time.time() - 12 * 3600))}))]

    def parse(self, response, **kwargs):
        for article in reversed(response.json()['data']):
            item = ArticlesItem()
            item['title'] = article['article_title']
            item['link'] = "https://www.infoq.cn/article/{}".format(article['uuid'])
            item['description'] = article['article_summary']
            item['source'] = 'infoq_articles'
            yield item
        if self.request_index == 0:
            self.request_index += 1
            yield scrapy.Request("https://www.infoq.cn/public/v1/my/recommond", headers=self.headers, method='POST',
                                 body=json.dumps({'size': 12, }))
