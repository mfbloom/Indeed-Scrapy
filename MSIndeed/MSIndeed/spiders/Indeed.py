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
    #rules=(Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="resultsCol"]/div/a/span/span',)), callback="parse_page", follow= True),)

    def start_requests(self):
        for i in xrange(1000):
            yield self.make_requests_from_url('http://www.indeed.com/jobs?q=PSEG+OR+%22Con+Edison%22&l=Huntington+Station%2C+NY&start=%d' %i)
            
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
            
    def parse_url(self,response):
        print "******RESPONSE URL******"
        jobs = scrapy.Selector(response).xpath('//table')
        
        myJob = MsindeedItem()
        for job in jobs:
            myJob['positionTitle'] = jobs.xpath('//*[@id="Title"]/text()').extract()
            myJob['positionDescription'] = jobs.xpath('//*[@id="Job Description"]/text()').extract()
            myJob['positionLocation'] = jobs.xpath('//*[@id="Location"]/text()').extract()
            yield myJob

        pass
        
    