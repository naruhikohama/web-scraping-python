# Web Scraping with Python

Web Scraping with Python Tools

There are 3 main tools to web scrape with python: beautiful soup, selenium and scrapy.

Beautiful soup is great if you have simple pages and itens in the page don't rely on js or user interaction to get the data. 
Selenium works better for controlling mouse and keyboard for interactions. It can access pages like a user would do, different from a beautiful soup, where it crawls though the page code, selenium interacts directly with the page. The downside is that is very slow to crawl through sites.
Lastly you have scrapy, which is fast but is a bit more difficult to program if you compare to the previous tools. 

## XPath

XPath is an expression language to search for text inside HTML documents (similar to regex is for strings).

- `//h1` will return all h1 results
- `//h1[1]` will return the first h1 ocurrence
- `//div[@class="full-script"]` will return divs with the class full script. Use `@` symbol before the atribute you are looking for
- `//p[(@class="plot1") or (@class="plot2")]` will return p with both classes inside the square brackets
- `//p[contains(@class, "plot")]` will return all ps with classes that contains the word "plot", so "plot2" would also be returned