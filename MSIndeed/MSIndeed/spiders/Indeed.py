import scrapy
import urlparse
from urlparse import urlparse
from urlparse import urljoin
import urllib2
import os
from bs4 import BeautifulSoup
from urlparse import urljoin
from scrapy.spiders import BaseSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector


from MSIndeed.items import MsindeedItem
from _cffi_backend import callback
from urlparse import urlparse

class myspider(CrawlSpider):
    name = "myspider"
    allowed_domains = ["indeed.com","brassring.com"]
    start_urls = ('http://www.indeed.com/jobs?q=PSEG+OR+%22Con+Edison%22&l=Huntington+Station%2C+NY',)
    rules=(Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@class="pagination"]',)), callback="parse_page", follow= True),)


    def parse(self, response):
        print "****STEP 1****"
        jobs = scrapy.Selector(response).xpath('//*[@id="resultsCol"]/div/h2')

        myLinks = []
        #for question in questions:
            #myLink = MsindeedItem()
            #myLink['positionURL'] 
        urls= jobs.xpath('a/@href').extract()
            #item['employeeName'] = question.xpath('h2/a/strong/text()').extract()
            #item['positionTitle'] = question.xpath('div/ul/li/text()').extract()
        print urls
        for link in urls:
            yield Request(urljoin(response.url, link[1:]),callback=self.parse_url)
            
        #for link in myLinks:
            #tempURL = self.make_requests_from_url(link)
                #yield Request(url=link,callback=self.parse_data(response))
            #yield self.make_requests_from_url(link)
    def parse_url(self,response):
        
        print "******RESPONSE URL******"
        print response.url
        jobs = scrapy.Selector(response).xpath('//*[@class="TEXT"]')
        title = jobs.xpath('text()').extract()
        print title

        pass
        
    