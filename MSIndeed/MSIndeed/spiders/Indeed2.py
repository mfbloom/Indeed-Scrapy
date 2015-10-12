import scrapy
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.contrib.linkextractors import LinkExtractor

from MSIndeed.items import MsindeedItem

#from spider.settings import JsonWriterPipeline
    
class Indeed2 (CrawlSpider):
    name = 'indeed2'
    allowed_domains = ['indeed.com']
    start_urls = ['http://www.indeed.com/jobs?q=Utility+(security+or+Infrastructure)&l=Huntington+Station,+NY&radius=50']
    
    def parse(self,response):
        hxs = scrapy.Selector(response)
        
        #divs = hxs.xpath('//h2')        
        
        item = []
        #for a in divs.xpath('.//a'):
        for a in hxs.css(".result"):
            item = MsindeedItem()
            #urlTemp = a.xpath('.//h2/a/@href')
            #print urlTemp
            item['positionURL'] = a.xpath('.//h2/a/@href').extract()
            tempURL = item['positionURL']
            item['positionTitle']= a.xpath('.//h2/a/text()').extract()
            item['companyName'] = a.xpath('.//span[1]/span/text()').extract()
            #item['numberOffriends']= titles.select("some path here").extract().pop()    
            #items.append(item)
            #yield item
            
            if not tempURL:
                url = response.urljoin(tempURL)
                print "****OH NO*****" +url
                posDescRequest =  scrapy.Request(url,callback=self.parse_position_contents)
                posDescRequest.meta['item'] = item
                yield posDescRequest
            #print url
            

        ##look to see if there is a next page Scrapy can follow        
        next_page = hxs.css("#next-pagination > a::attr('href')")
        print next_page
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url,self.parse)
            
    def parse_position_contents(self, response):
        for sel in response.xpath('//td[@class=snip]'):
            item = MsindeedItem()
            item['positionDescription'] = sel.xpath('p/text()').extract()
            item['positionDesccriptionURL'] = response.url
            #self.logger.info("Visited %s", response.url)
            print "I GOT HERE YES"
            #item['link'] = sel.xpath('a/@href').extract()
            #item['desc'] = sel.xpath('text()').extract()
            return item