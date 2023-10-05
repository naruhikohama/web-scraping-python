from selenium import webdriver 
import pandas as pd

website = 'https://www.audible.com/search'
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'    
driver = webdriver.Chrome(path)
driver.get(website) 

driver.maximize_window() 

container = driver.find_element('xpath', '//div[@class="adbl-impression-container "]')
products = container.find_elements('xpath', './li')

book_title = []
book_author = []
book_length = []

for product in products:
    title = product.find_element('xpath', './/h3[contains(@class, "bc-heading")]').text
    author = product.find_element('xpath', './/li[contains(@class, "authorLabel")]').text
    runtime = product.find_element('xpath', './/li[contains(@class, "runtimeLabel")]').text
    print(title, author, runtime)

    book_title.append(title)
    book_author.append(author)  
    book_length.append(runtime)

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index = False)


# .//li[contains(@class, "productListItem")]

# This means that the "products" variable will be:

# products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')