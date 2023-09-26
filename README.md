# Web Scraping with Python

Web Scraping with Python Tools

There are 3 main tools to web scrape with python: beautiful soup, selenium and scrapy.

Beautiful soup is great if you have simple pages and itens in the page don't rely on js or user interaction to get the data. 
Selenium works better for controlling mouse and keyboard for interactions. It can access pages like a user would do, different from a beautiful soup, where it crawls though the page code, selenium interacts directly with the page. The downside is that is very slow to crawl through sites.
Lastly you have scrapy, which is fast but is a bit more difficult to program if you compare to the previous tools. 

## XPath

XPath is an expression language to search for text inside HTML documents (similar to regex is for strings).

- `//h1` will return all h1 results
- `//h1/text()` This ending (/text()) will return the text inside the node
- `//h1[1]` will return the first h1 ocurrence
- `//h1/div` will return the div that are children of h1
- `//h1/..` will return the parent of this node
- `//h1/*` will return all the children nodes of this tag
- `//div[@class="full-script"]` will return divs with the class full script. Use `@` symbol before the atribute you are looking for
- `//p[(@class="plot1") or (@class="plot2")]` will return p with both classes inside the square brackets
- `//p[contains(@class, "plot")]` will return all ps with classes that contains the word "plot", so "plot2" would also be returned

## Selenium
Selenium usa algumas interações com códigos javascript para extrair informações da página através do navegador.

Para isso, é necessário uma interface que vai traduzir os comandos do script para comandos que seriam executados em uma página(scroll, click, digitar em caixas de textos e/ou inputs). Essa interface é o webdriver e cada navegador tem seu próprio webdriver. Para esse curso, será usado o webdriver do Chrome. É importante saber qual a versão do chrome você está usando e se o webdriver é compatível com sua versão. Para versões mais novas do chrome, acesse esse [link](https://googlechromelabs.github.io/chrome-for-testing/#stable) e para versões não tão novas e/ou do tipo LTS, acesse esse [link](https://chromedriver.chromium.org/downloads).