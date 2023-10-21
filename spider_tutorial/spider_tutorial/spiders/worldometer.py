import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath("//h1/text()").get() 
        countries = response.xpath("//td/a")

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # retrieve data with an absolute url
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

            # retrieve data with a relative url
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': country_name})
    
    def parse_country(self, response):
        rows = response.xpath('(//table[contains(@class, "table")])[1]/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country': response.request.meta['country_name'],
                'year': year,
                'population': population,
            }
