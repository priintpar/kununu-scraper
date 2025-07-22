#Kununu Review Scraper by mantikor17.com
#
#
#install scrapy https://doc.scrapy.org/en/latest/intro/install.html
#start from console with
#scrapy crawl kununu -o bewertungen.csv

from os import name
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "kununu"

    def start_requests(self):
        urls = [
            #'https://www.kununu.com/de/volkswagen/kommentare',
            'https://www.kununu.com/de/telefonica-germany/kommentare',
            #'https://www.kununu.com/de/tesla-deutschland/kommentare',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for rating in response.css('article.index__contentBlock__7vKo-'):
            yield {
                'Firma': rating.css('a.reviews-share-button').xpath('./@href').get(),
                'Datum': rating.css('time').xpath('./@datetime').get(),
                'Bewertung': rating.css('span.index__score__16yy9::text').get(),
                'Empfehlung': rating.css('span.p-tiny-bold::text').get(),
                'Position': rating.css('div.index__employmentInfoBlock__27ro4').xpath('./b').get(),
                'Weitere Informationen': rating.css('span.index__sentence__3PKUg::text').get()
            }

        next_page = response.css('a.index__button__1mqIU').xpath('./@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)