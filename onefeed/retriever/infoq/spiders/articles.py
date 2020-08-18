# -*- coding: utf-8 -*-
import json
import time

from ..items import ArticlesItem
import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'infoq_articles'
    allowed_domains = ['www.infoq.cn']

    def start_requests(self):
        headers = {'origin': 'https://www.infoq.cn', 'referer': 'https://www.infoq.cn', 'host': 'www.infoq.cn'}
        return [scrapy.Request("https://www.infoq.cn/public/v1/my/recommond", headers=headers, method='POST', body=json.dumps({'size': 12})),
                scrapy.Request("https://www.infoq.cn/public/v1/my/recommond", headers=headers, method='POST',
                               body=json.dumps({'size': 12, 'score': int(1e3 * (time.time() - 12 * 3600))}))
                ]

    def parse(self, response):
        for article in response.json()['data']:
            item = ArticlesItem()
            item['title'] = article['article_title']
            item['link'] = "https://www.infoq.cn/article/{}".format(article['uuid'])
            item['description'] = article['article_summary']
            item['source'] = 'infoq_articles'
            yield item
