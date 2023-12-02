import scrapy
from scrapy_splash import SplashRequest

class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    start_urls = ["https://www.adamchoi.co.uk/"]

    script = """
    function main(splash, args)
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
        print(response.body)
