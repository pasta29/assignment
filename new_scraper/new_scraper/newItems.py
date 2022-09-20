import scrapy

class NewsItem(scrapy.Item):
    title = scrapy.Field()  #storage array type
    link = scrapy.Field()
    description = scrapy.Field()
    pubDate = scrapy.Field()
    
