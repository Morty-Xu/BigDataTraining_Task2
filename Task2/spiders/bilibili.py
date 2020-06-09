import scrapy
import json
from Task2.items import Task2Item

# 爬取 b站 2020-05-01至 2020-05-31一个月以来发布的所有鬼畜视频
class BilibiliSpider(scrapy.Spider):
    name = 'Task2'
    allowed_domains = ['s.search.bilibili.com']
    prefix = 'https://s.search.bilibili.com'

    # 起始请求，主要为了获取页数 numPages
    start_urls = [
        'https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_32548301302379645'
        '&main_ver=v3&search_type=video&view_type=hot_rank&order=click'
        '&copy_right=-1&cate_id=22&pagesize=20&time_from=20200501&time_to=20200531'
    ]

    # 第一步：获取页数 numPages
    def parse(self, response):
        r = json.loads(response.text)
        numPages = r['numPages']

        for i in range(numPages):
            url = 'https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_32548301302379645' \
                  '&main_ver=v3&search_type=video&view_type=hot_rank&order=click' \
                  '&copy_right=-1&cate_id=22&page={}&pagesize=20&time_from=20200501&time_to=20200531' . format(i + 1)
            yield scrapy.Request(url=url, callback=self.parse_detail)


    def parse_detail(self, response):
        result = json.loads(response.text)['result']

        for i in range(len(result)):
            item = Task2Item()
            item['rank'] = (result[i]['rank_index']) * 20 + result[i]['rank_offset']
            item['author'] = result[i]['author']
            item['arcurl'] = result[i]['arcurl']
            item['description'] = result[i]['description']
            item['favorites'] = result[i]['favorites']
            item['play'] = result[i]['play']
            item['rank_score'] = result[i]['rank_score']
            item['tag'] = result[i]['tag'].replace(',', '&&')
            item['title'] = result[i]['title']
            item['video_review'] = result[i]['video_review']
            yield item

