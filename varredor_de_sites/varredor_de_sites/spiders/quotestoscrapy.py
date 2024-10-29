from typing import Any, Iterable
import scrapy
from scrapy.http import Response

class QuotesToScrapeSpider(scrapy.Spider):
    #Identidade (nome do bot)
    name = 'frasebot'
    #Request
    def start_requests(self): 
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #Response
    def parse(self, response):
        #Aqui sera feito o processamento das paginas
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                'autor': elemento.xpath(".//small[@class='author']/text()").get(),
                'tags': elemento.xpath(".//a[@class='tag']/text()").getall()
            }
        
        #como varrer varias paginas
        

    