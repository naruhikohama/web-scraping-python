import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in product_container:
            title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').get()
            runtime = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get().split(':')[1].strip()

            print(title, author, runtime)

            yield {
                'title': title,
                'author': author,
                'length': runtime
            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page_url = pagination.xpath('//span[contains(@class, "nextButton")]/a/@href').get()

        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)
