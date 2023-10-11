from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from dotenv import load_dotenv
import os

def get_tweet(element):
    try:
        tweet = element.find_element('xpath', './/article[contains(@data-testid, "tweet")]')
        user = element.find_element('xpath', './/div[contains(@data-testid, "User-Name")]//a//span[not(contains(text(),"@"))]/text()')
        user_at = element.find_element('xpath', './/div[contains(@data-testid, "User-Name")]//a//span[contains(text(),"@")]/text()')
        return tweet.text, user, user_at
    except:
        return None

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

website = 'https://twitter.com/'
# path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe' 
options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.get(website)

driver.maximize_window()

login = driver.find_element('xpath', '//a[@href="/login"]')
login.click()

# login_box = driver.find_element('xpath', '//input[contains(@autocomplete, "username")]') 
login_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@autocomplete, "username")]')))
login_box.send_keys(EMAIL)

next_button = driver.find_element('xpath', '//div[@role = "button"]//span[contains(text(), "Avançar") or contains(text(), "Next")]')
next_button.click()

password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@name, "password")]')))
password.send_keys(PASSWORD)

login_button = driver.find_element('xpath', '//div[@data-testid = "LoginForm_Footer_Container"]//div[@role="button"]')
login_button.click()

search_button = driver.find_element('xpath', '//input[@enterkeyhint="search"]')
search_button.send_keys('python')

tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))

sleep(10)