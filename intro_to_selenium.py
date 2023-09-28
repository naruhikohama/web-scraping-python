from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
from time import sleep

def launchBrowser(website, webdriver_path):
    driver = webdriver.Chrome(webdriver_path)
    driver.get(website)

    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    while True:
        sleep(5)
        pass

website = 'https://www.adamchoi.co.uk/overs/detailed'  
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'

launchBrowser(website = website, webdriver_path = path)