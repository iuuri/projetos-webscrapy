from typing import Any, Iterable
import scrapy
from scrapy.http import Response

class GoodReadsSpider(scrapy.Spider):

    #Identidade (nome do bot)
    name = 'extractbot'
    #Request
    def start_requests(self): 
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    #Response
    def parse(self, response):
        #Aqui sera feito o processamento das paginas
        for elemento in response.xpath("//div[@class='quoteDetails']"):
            yield {
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': elemento.xpath(".//div[@class='quoteFooter']//div//a/text()").getall()
            }
        
        try:
            link_proxima_pagina = response.xpath('//a[@class="next_page"]//@href').get()
            if link_proxima_pagina is not None:
                link_proxima_pagina_completo = response.urljoin(link_proxima_pagina)
                yield scrapy.Request(url=link_proxima_pagina_completo, callback=self.parse)
        
        except:
            print('Todas as paginas extraidas.')