from typing import Any, Iterable
import scrapy
import pandas as pd

class ProgramaLeiloesSpider(scrapy.Spider):
    name = 'extractbot'
    
    # Lista para armazenar os dados
    extracted_data = []

    def start_requests(self): 
        urls = ['https://programaleiloes.com/agenda']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extrair todos os links dos cards e seguir cada um para extrair os detalhes
        links_cards = response.xpath("//div[@class='leiloes-area']//li//@href").getall()
        
        for link_card in links_cards:
            yield response.follow(url=link_card, callback=self.parse_details)

    def parse_details(self, response):
        # Extrair os dados específicos de cada página de detalhes
        titulo = response.xpath("//div[@class='titulo']//h1//text()").get()
        dia = response.xpath("//time[@datetime]//span[contains(@class, 'dia')]/text()").get()
        mes = response.xpath("//time[@datetime]//span[contains(@class, 'mes')]/text()").get()
        hora = response.xpath("//div[@class='hora']//p/text()").get() 
        local = response.xpath("//span[@class='cidade']//text()").get()

        # Verificar se há informações de transmissão e definir valor padrão caso esteja vazio
        transmisao = response.xpath("//div[@class='transmissao']//img//@alt").getall()
        transmisao = transmisao if transmisao else ['Sem transmissão']
        
        # Armazenar os dados extraídos na lista
        self.extracted_data.append({
            'Titulo': titulo,
            'Dia': dia,
            'Mes': mes,
            'Hora': hora,
            'Local': local,
            'Transmissão': ', '.join(transmisao)  # Converte a lista em string, separada por vírgulas
        })

    def close(self, reason):
        # Converter os dados armazenados em um DataFrame pandas e salvar em Excel
        df = pd.DataFrame(self.extracted_data)
        df.to_excel("leiloes.xlsx", index=False)
