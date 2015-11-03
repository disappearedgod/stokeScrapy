# -*- coding: utf-8 -*-

# Scrapy settings for stokeScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stokeScrapy'

SPIDER_MODULES = ['stokeScrapy.spiders']
NEWSPIDER_MODULE = 'stokeScrapy.spiders'
download_delay=1
# ITEM_PIPELINES={'stokeScrapy.pipelines.stokeScrapyPipeline':300}
ITEM_PIPELINES = ['stokeScrapy.pipelines.MongoDBPipeline', ]
MONGODB_SERVER = "localhost" 
MONGODB_PORT = 27017 
MONGODB_DB = "DFCFStock" 
MONGODB_COLLECTION = "stock"
COOKIES_ENABLED=False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stokeScrapy (+http://www.yourdomain.com)'
#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'stokeScrapy.spiders.UserAgentMiddle.UserAgentMiddle':400
    }


