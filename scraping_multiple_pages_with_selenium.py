from selenium import webdriver 
import pandas as pd
from time import sleep

website = 'https://www.audible.com/search'
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'   
options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-error")
# options.add_argument("--ignore-ssl-errors") 
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
# options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(path, options=options)
driver.get(website) 

driver.maximize_window() 
sleep(2)

container = driver.find_element('xpath', '//div[@class="adbl-impression-container "]')
products = container.find_elements('xpath', './/li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    title = product.find_element('xpath', './/h3[contains(@class, "bc-heading")]').text
    author = product.find_element('xpath', './/li[contains(@class, "authorLabel")]').text
    runtime = product.find_element('xpath', './/li[contains(@class, "runtimeLabel")]').text
    print(title, author, runtime)

    book_title.append(title)
    book_author.append(author.split(':')[1].strip())  
    book_length.append(runtime.split(':')[1].strip())

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index = False)

