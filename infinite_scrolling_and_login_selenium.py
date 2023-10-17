from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from dotenv import load_dotenv
import os
import pandas as pd


def get_tweet(element):
    try:
        tweet = element.find_element('xpath', './/div[contains(@data-testid, "tweetText")]')
        user = element.find_element('xpath', './/div[contains(@data-testid, "User-Name")]//a//span[not(contains(text(),"@"))]')
        user_at = element.find_element('xpath', './/div[contains(@data-testid, "User-Name")]//a//span[contains(text(),"@")]')
        return [user.text, user_at.text, tweet.text]
    except:
        return None, None, ''

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')

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

try:
    print(f'Chegou ao começo do primeiro try\n')
    sleep(2)
    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@name, "password")]')))
    password.send_keys(PASSWORD)

except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
    print(f'Chegou no primeiro except\n')
    sleep(2)
    double_check = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete]")))
    print(f'Precisa enviar o username {TWITTER_USERNAME} para o campo\n')
    double_check.send_keys(TWITTER_USERNAME)

    sleep(1)
    next_button = driver.find_element('xpath', '//div[@role = "button"]//span[contains(text(), "Avançar") or contains(text(), "Next")]')
    next_button.click()

password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@name, "password")]')))
password.send_keys(PASSWORD)

login_button = driver.find_element('xpath', '//div[@data-testid = "LoginForm_Footer_Container"]//div[@role="button"]')
login_button.click()

search_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@enterkeyhint="search"]')))
search_button.send_keys('python')
search_button.send_keys(Keys.ENTER)

last_height = driver.execute_script("return document.body.scrollHeight")
counter = 0
user_data = []
user_at_data = []
tweet_text_data = []
last_tweets = []

while counter < 20: # scroll down 20 times
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    counter += 1
    print(f'Counter: {counter}')
    if new_height == last_height:
        break
    last_height = new_height

    current_tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))
    tweets = [tweet for tweet in current_tweets if tweet not in last_tweets]
    if tweets is not None:
        print(f"Number of tweets: {len(tweets)}")
        for tweet in tweets:
            user, user_at, tweet_text = tuple(get_tweet(tweet))
            print(f'{tweet_text}\n')
            text = " ".join(tweet_text.split())
            if user is not None:
                user_data.append(user)
                user_at_data.append(user_at)
                tweet_text_data.append(text)
    
    last_tweets = tweets

df_tweets = pd.DataFrame({'user': user_data, 'user_at': user_at_data, 'tweet': tweet_text_data})
df_tweets.to_csv('tweets.csv', index = False)

sleep(10)