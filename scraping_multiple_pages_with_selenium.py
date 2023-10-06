from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep

website = 'https://www.audible.com/search'
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'   
options = Options()
options.headless = True # run in the background
options.add_argument("--window-size=1920,1080")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(path, options=options)
driver.get(website) 

# driver.maximize_window() 
# sleep(2)

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

