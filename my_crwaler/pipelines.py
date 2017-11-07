# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import my_crwaler.utils.common as utils


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyCrwalerPipeline(object):
    def process_item(self, item, spider):
        return item


class TtmeijuItemPipeline(object):
    # def process_item(self, item, spider):
    #     x = item['xunleiUrl']
    #     return item

    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 固定用法 引入配置文件
    @classmethod
    def from_settings(cls, settings):
        parsms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        #
        dbpool = adbapi.ConnectionPool("MySQLdb", **parsms)

        return cls(dbpool)

    def process_item(self, item, spider):
        x = item
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异步异常


    # 处理异步异常
    def handle_error(self, failure):
        print(failure)

    def do_insert(self, cursor, item):
        # 执行逻辑
        # x = item
        for i in range(len(item['baiduUrl'])):
            insert_sql = """replace into ttmeiju(baiduurl, xunleiurl, xiaomiurl, ed2url, bturl, kind, size, season,chinesetitle,
              id_object,release_time,episode)  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """
            cursor.execute(
                insert_sql % (item['baiduUrl'][i], item['xunleiUrl'][i], item['xiaomiUrl'][i], item['ed2Url'][i],
                              item['btUrl'][i], item['kind'][i], item['size'][i], item['season'][i],
                              item['chinese_title'][i], item['object_id'][i], item['release_time'][i],
                              item['episode'][i]))
