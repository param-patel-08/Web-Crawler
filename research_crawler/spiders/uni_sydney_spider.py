import scrapy
from research_crawler.items import ResearchCrawlerItem

class UniSydneySpider(scrapy.Spider):
    name = "uni_sydney"
    allowed_domains = ["sydney.edu.au"]
    start_urls = [
        "https://www.sydney.edu.au/arts/our-research/research-areas.html"
    ]

    def parse(self, response):
        for area in response.css('li.link-list__item'):
            item = ResearchCrawlerItem()
            item['title'] = area.css('a::text').get()
            item['link'] = response.urljoin(area.css('a::attr(href)').get())
            item['description'] = None
            item['university'] = "University of Sydney"
            yield item
