import scrapy
from scrapy_splash import SplashRequest

class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    start_urls = ["https://www.adamchoi.co.uk/"]

    script = """
    function main(splash, args)
      splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0')
      splash.private_mode_enabled = false
      assert(splash:go(args.url))
      assert(splash:wait(1))
      all_matches = assert(splash:select_all('label.btn.btn-sm.btn-primary'))
      all_matches[2]:mouse_click()
      assert(splash:wait(1))
      splash:set_viewport_full()
      return {
        html = splash:html(),
        png = splash:png()
      }
    end

    """

    def start_requests(self):
        yield SplashRequest(
            url="https://www.adamchoi.co.uk/overs/detailed",
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source": self.script,
                "wait": 1,
            },
        )

    def parse(self, response):
        response.xpath('//tr')

        for row in response.xpath('//tr'):
            date = row.xpath('./td[1]/text()').get()
            home_team = row.xpath('./td[2]/text()').get()
            score = row.xpath('./td[3]/text()').get()
            away_team = row.xpath('./td[4]/text()').get()

            yield {
                'date': date,
                'home_team': home_team,
                'score': score,
                'away_team': away_team
            }
