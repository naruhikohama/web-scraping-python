from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

website = 'https://twitter.com/'
# path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe' 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
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

# login_button = driver.find_element('xpath', '//div[@data-testid = "LoginForm_Footer_Container"]//div[@role="button"]')
# login_button.click()

sleep(10)