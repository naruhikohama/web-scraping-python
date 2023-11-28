import scrapy


class ChronomaxSpider(scrapy.Spider):
    name = "chronomax"
    allowed_domains = ["www.chronomax.com.br"]
    start_urls = ["https://www.chronomax.com.br/index.php/Resultado"]

    def parse(self, response):
        pass
