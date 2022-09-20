"""code is for scraping website data
here I have used RSS(Rich Site Summary) of the website to fetch the relevant data, as website updates it's RSS feed on regular basis. So it's more feasible to use the RSS """
import re
import imp
import scrapy
from ..newItems import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['http://www.theguardian.com/international/rss']
    
    def striphtml(self,data):    #this will remove html tags
        p = re.compile(r'<.*?>')
        return p.sub('', data)

    def parse(self, response):
        for data in response.css('item'):  
            item = NewsItem()  #class object used for handling storage of data
            item['title'] = data.css('title::text').get()
            item['link'] = data.css('link::text').get()
            item['description'] = self.striphtml(data.css('description::text').get()) 
            item['pubDate'] = data.css('pubDate::text').get()
        
            yield item 
