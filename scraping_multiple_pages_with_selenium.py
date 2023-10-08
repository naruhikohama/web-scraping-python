from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep

website = 'https://www.audible.com/search'
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'   
options = Options()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(path, options=options)
driver.get(website) 

pagination = driver.find_element('xpath', '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements('xpath', './li')
last_page = int(pages[-2].text) # -1 is next button, -2 is last page

current_page = 1 

book_title = []
book_author = []
book_length = []
while current_page <= last_page:
    # sleep(1)
    # container = driver.find_element('xpath', '//div[@class="adbl-impression-container "]')
    # products = container.find_elements('xpath', './/li[contains(@class, "productListItem")]')
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="adbl-impression-container "]')))
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))
    print(current_page)
    for product in products:
        title = product.find_element('xpath', './/h3[contains(@class, "bc-heading")]').text
        author = product.find_element('xpath', './/li[contains(@class, "authorLabel")]').text
        runtime = product.find_element('xpath', './/li[contains(@class, "runtimeLabel")]').text
        # print(title, author, runtime)

        book_title.append(title)
        book_author.append(author.split(':')[1].strip())  
        book_length.append(runtime.split(':')[1].strip())
    
    current_page += 1

    try:
        next_page = driver.find_element('xpath', '//span[contains(@class, "nextButton")]') 
        next_page.click()

    except:
        print('No more pages to load.')
        pass

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index = False)

