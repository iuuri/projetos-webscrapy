# https://br.indeed.com/jobs?q=python&l&from=searchOnHP&vjk=ef1205fc3520566b
import scrapy


class IndeedPythonSpider(scrapy.Spider):
    # identidade
    name = 'vagasbot'
    # request

    def start_requests(self):
        urls = [
            'https://br.indeed.com/jobs?q=python&l&from=searchOnHP&vjk=ef1205fc3520566b']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # response

    def parse(self, response):
        # varrer cada grupo de informação e seus detalhes
        for item in response.xpath("//td[@class='resultContent']"):
            yield {
                'cargo': item.xpath(".//span[1]/text()").get(),
                'nome empresa': item.xpath(".//span[@class='companyName']/text()").get(),
                'local': item.xpath(".//div[@class='companyLocation']/span/text()").get(),
                'link': 'https://br.indeed.com' + item.xpath(".//a/@href").get()
            }

        try:
            link_proxima_pagina = response.xpath("//a[@data-testid='pagination-page-next']/@href").get()
            print('#'*10)
            print(link_proxima_pagina)
            print('#'*10)
            if link_proxima_pagina is not None:
                link_completo = 'https://br.indeed.com' + link_proxima_pagina 
                print('*'*10)
                print(link_completo)
                print('*'*10)
                yield scrapy.Request(url=link_completo, callback=self.parse)
            
        except Exception as error:
            print(error)
            print('Chegamos na última página')