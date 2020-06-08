# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Task2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()  # 视频作者

    arcurl = scrapy.Field()  # 视频 url

    description = scrapy.Field() # 视频作品描述

    favorites = scrapy.Field() # 三连量

    play = scrapy.Field() # 播放量

    # rank_index = scrapy.Field() # 排名页数

    # rank_offset = scrapy.Field() # 页内排序

    rank = scrapy.Field() # 排名

    rank_score = scrapy.Field() # 排名分数

    tag = scrapy.Field() # 标签

    title = scrapy.Field() # 标题

    video_review = scrapy.Field() # 弹幕数

