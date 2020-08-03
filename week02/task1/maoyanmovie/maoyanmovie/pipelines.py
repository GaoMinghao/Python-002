# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MaoyanmoviePipeline:
    def __init__(self, dbInfo):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.username = dbInfo['username']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            dbInfo=crawler.settings.get("DB_INFO")
        )

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            db=self.db
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        release_date = item['release_date']
        try:
            sql = "insert into `maoyan_movie` (`name`,`type`,`release_date`) value (%s,%s,%s)"
            self.cur.execute(sql, (title, movie_type, release_date))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
