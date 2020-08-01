# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'db': 'test'
}


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        release_date = item['release_date']
        conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db']
        )
        cur = conn.cursor()
        try:
            sql = "insert into `maoyan_movie` (`name`,`type`,`release_date`) value (%s,%s,%s)"
            cur.execute(sql, (title, movie_type, release_date))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()
        return item
