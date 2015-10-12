# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MsindeedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    positionLink = scrapy.Field()
    positionURL = scrapy.Field()
    positionTitle = scrapy.Field()
    #//*[@id="job_summary"]/p[1]/b[3]
    #//*[@id="job_header"]/b/font
    
    positionDuraction = scrapy.Field()
    #//*[@id="job_summary"]/p[1]/b[4]
    
    companyName = scrapy.Field()
    #//*[@id="job_header"]/span[1]
    
    positionLocation = scrapy.Field()
    #//*[@id="job_header"]/span[2]
    
    salaryMax = scrapy.Field()
    salaryMin = scrapy.Field()
    
    positionDescription = scrapy.Field()
    positionDescriptionURL = scrapy.Field()
    
    #//*[@id="job_summary"]/p[2]
    
    educationRequired = scrapy.Field()
    #//*[@id="job_summary"]/ul[1]/li
    
    
    
    pass
