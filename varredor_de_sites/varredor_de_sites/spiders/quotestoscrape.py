from typing import Iterable
import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
    #Identidade
    name = 'frasebot'
    # Request
    def start_requests(self):
        #definir urls para varredura
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # Response
    def parse(self, response):
        pass
    #o que deve ser processador do response
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)