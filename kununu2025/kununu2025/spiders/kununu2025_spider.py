import scrapy

class Kununu2025Spider(scrapy.Spider):
    name = "kununu2025"
    
    async def start(self):
       urls = ['https://www.kununu.com/de/gtue/kommentare',]
       for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for rating in response.css("article.index-module__contentBlock__foHOO"):
            yield {
                'Firma': rating.xpath('//title/text()').get(),
                'Datum': rating.css('time.text-dark-63::text').get(),
                'Bewertung': rating.css('span.index__score__BktQY::text').get(),
                'Empfehlung': rating.css('span.p-tiny-bold::text').get(),
                'Position': rating.css('div.index__employmentInfoBlock__wuOtj > b::text').get(),
                'Weitere Informationen': rating.css('span.index__sentence__j5Cc3::text').get()
            }

        next_page = response.xpath('/html/body/div/div/div[1]/main/div/div[4]/div/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)