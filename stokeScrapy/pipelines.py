# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import codecs
import json

class stokeScrapyPipeline(object):

    def __init__(self):

        self.file=codecs.open("stokeScrapy.json",mode="wb",encoding='utf-8')
        self.file.write('{"hah"'+':[')
    def process_item(self, item, spider):
        line = json.dumps(dict(item))+","
        self.file.write(line.decode("unicode_escape"))

        return item
##############################################################
# import pymongo
# from scrapy.conf import settings
# from scrapy.exceptions import DropItem
# from scrapy import log


# #MongoDBPipeline
# class MongoDBPipeline( object ):
#    def __init__( self ):
#      connection = pymongo.MongoClient(
#        settings[ 'MONGODB_SERVER' ],
#        settings[ 'MONGODB_PORT' ]
#      )
#      db = connection[settings[ 'MONGODB_DB' ]]
#      self .collection = db[settings[ 'MONGODB_COLLECTION' ]]
   
#    def process_item( self , item, spider):
#      valid = True
#      for data in item:
#        if not data:
#          valid = False
#          raise DropItem( "Missing {0}!" . format (data))
#      if valid:
#        self .collection.insert( dict (item))
#        log.msg( "Stoke added to MongoDB database!" ,
#            level = log.DEBUG, spider = spider)
#      return item


#######################################################

