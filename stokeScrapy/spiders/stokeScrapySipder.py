from scrapy.spider import Spider
from scrapy.selector import Selector
from stokeScrapy.items import stokeScrapyItem
import re
from scrapy import log
class stokeScrapySpider(Spider):

    name = "stokeScrapy"
    allowed_domains=['eastmoney.com']
    start_urls = ["http://quote.eastmoney.com/stocklist.html#sh"]

    def parse(self, response):

        sel = Selector(response)
        cont=sel.xpath('//div[@class="qox"]/div[@class="quotebody"]/div/ul')[0].extract()
        item = stokeScrapyItem()

        for temp in re.findall(r'<li>.*?<a.*?target=.*?>(.*?)</a>',cont):
            item["stockName"]=temp.split("(")[0].encode('utf-8')
            item["stockCode"]=("sh"+temp.split("(")[1][:-1]).encode('utf-8')
            log.msg(temp.encode('utf-8'),level="INFO")
            yield item

        #item["stockCode"]="+------------------------------------------------------------------+"
        #yield item
        cont1=sel.xpath('//div[@class="qox"]/div[@class="quotebody"]/div/ul')[1].extract()

        for temp2 in re.findall(r'<li>.*?<a.*?target=.*?>(.*?)</a>',cont1):
            item["stockName"]=temp2.split("(")[0].encode('utf-8')
            item["stockCode"]=("sz"+temp2.split("(")[1][:-1]).encode('utf-8')
            #log.msg(temp2.encode('utf-8'),level="INFO")
            yield item