# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class FlipkartScPipeline:
    def process_item(self, item, spider):
        return item


class SavingToPostgresPipeline:

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Postgresql',
            database='scrapy_db',
            port=5432
        )
        

    def proccess_item(self, items, spider):
        self.store_db(items)
        return items

    def store_db(self, items):
        try:
            self.curr.execute(""" insert into scrapy (product_name, product_price, product_ram_rom, product_bettry, product_imagelink) values (%s, %s, %s)""", (
                items['product_name'],
                items['product_price'],
                items['product_ram_rom'],
                items['product_bettry'],
                items['product_imagelink'],
            ))
        except BaseException as e:
            print(e)
        self.connection.commit()