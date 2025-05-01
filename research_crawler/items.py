# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ResearchCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    university = scrapy.Field()
    