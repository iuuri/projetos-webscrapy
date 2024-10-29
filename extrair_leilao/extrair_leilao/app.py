from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from extrair_leilao.spiders.programaleiloes import ProgramaLeiloesSpider  

if __name__ == '__main__':
    print("Iniciando o processo de extração de dados...")
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(ProgramaLeiloesSpider)
    process.start()
    print("Processo de extração concluído.")
