# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class Task2Pipeline(object):
    def __init__(self):
        self.file = open('bilibili.csv', 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)

    # 对 spider 传递过来的 item 对象进行处理
    def process_item(self, item, spider):
        # 数据处理：比如缺失数据整理、删除；重复数据清理；不合理数据的整理


        # 数据存储
        self.writer.writerow(
            [item['rank'], item['author'], item['arcurl'], item['description'], item['favorites'], item['play'],
             item['rank_score'], item['tag'], item['title'], item['video_review']])

        return item

    def close_spider(self, spider):
        self.file.close()