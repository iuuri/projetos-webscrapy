import scrapy

class FiiScraperSpider(scrapy.Spider):
    # identidade
    name = 'fiibot'
    # Request
    def start_requests(self):
        urls = ['https://www.fundamentus.com.br/fii_resultado.php']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    # Response
    def parse(self, response):
        # Montar um xpath que retorna a linha
        for linha in response.xpath("//table"):
            yield {
                # Montar individualmente um xpath que retorna cada item daquela  linha
                'Nome': linha.xpath('//table//td[1]//span//a//text()').get()
                # 'Segmento': linha.xpath('.//td[2]//text()').get(),
                # 'Dividend Yield': linha.xpath('.//td[5]/text()').get(),
                # 'P/VP': linha.xpath('.//td[6]/text()').get(),
                # 'Valor de Mercado': linha.xpath('.//td[7]//div//text()').get(),
                # 'Liquidez': linha.xpath('.//td[8]//div//text()').get()
            }
