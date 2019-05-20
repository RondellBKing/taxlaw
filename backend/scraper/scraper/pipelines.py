# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import sqlite3

class MarinPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS lien_tb""")
        self.curr.execute("""create table lien_tb(
                recording_date real,
                doc_title text,
                involved text,
                )""")

    def process_item(self, item, spider):
        logging.warning('process_item is being called')
        self.store_db(item)
        print("From the pipeline: " + item['involved'])
        item.save()
        return item

    def store_db(self, item):
        self.cur.execute("""insert into lien_tb values (?,?,?)""",(
            item['recording_date'][0],
            item['doc_title'][0],
            item['involved'][0]
            ))
        self.conn.commit()
