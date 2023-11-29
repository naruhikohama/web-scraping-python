import scrapy


class ChronomaxSpider(scrapy.Spider):
    name = "chronomax"
    allowed_domains = ["www.chronomax.com.br"]
    # start_urls = ["https://www.chronomax.com.br/index.php/Resultado/index//0/S"]

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.chronomax.com.br/index.php/Resultado/index//0/S",
            callback=self.parse,
            headers={
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})

    def parse(self, response):
        corridas = response.xpath('//div[@class="event-listing"]//li[@class = "latest-news-item"]')

        for corrida in corridas:
            dia = corrida.xpath('.//div[@class = "news-day"]/text()').get()
            mes = corrida.xpath('.//div[@class = "news-month2"]/text()').get()
            ano = corrida.xpath('.//div[@class = "news-year"]/text()').get()
            yield {
                'prova': corrida.xpath('.//div[@class="news-title"]/text()').get().strip(),
                'local': corrida.xpath('.//p[@class="event-text"]/text()').get(),
                'link': corrida.xpath('.//div/@onclick').extract_first().strip().split("=", 1)[1].replace("'", ""),
                'data': ano + "-" + mes + "-" + dia
            }
    
            page = 0
            while page < 100:
                page += 1
                next_page = f"https://www.chronomax.com.br/index.php/Resultado/index/{page}/S"
                if next_page:
                    yield scrapy.Request(
                        url=next_page,
                        callback=self.parse
                    )

