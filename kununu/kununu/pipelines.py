import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class KununuPipeline(object):

    def process_item(self, item, spider):
        #item['rating'] = item['rating'].strip()
        #item['rating'] = float(item['rating'].replace(',', "."))

        item['Firma'] = item['Firma'].replace('https://www.kununu.com/de/', "").split('/', 1)[0]
        item['Datum'] = item['Datum'].split('T', 1)[0]
        if item['Empfehlung'] == None: item['Empfehlung'] = 'keine Angabe'
        if item['Position'] == None: item['Position'] = 'keine Angabe'
        item['Position'] = item['Position'].replace('<b>', "").replace('<!-- -->', "").replace('</b>', "")

        return item