from typing import Iterable
import scrapy
from scrapy.http import Request


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    # start_urls = ["https://www.audible.com/search"]

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(
            url="https://www.audible.com/search",
            callback=self.parse,
            headers={
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        audible_meta_data = []
        titles = []

        for product in product_container:
            title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').get()
            runtime = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get().split(':')[1].strip()

            # print(title, author, runtime)            

            yield {
                'title': title,
                'author': author,
                'length': runtime
            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page_url = pagination.xpath('//span[contains(@class, "nextButton")]/a[not(contains(@href,"page=26"))]/@href').get()

        # last_page = int(response.xpath('(//a[contains(@class, "pageNumberElement ")])[last()]//text()').get())

        if next_page_url:
            yield response.follow(next_page_url, 
                                  callback=self.parse, 
                                  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
                                  )
