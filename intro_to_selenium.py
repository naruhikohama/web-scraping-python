from selenium import webdriver 
# from selenium.webdriver.common.by import By
from time import sleep

def launchBrowser(website, webdriver_path):
    driver = webdriver.Chrome(webdriver_path)
    driver.get(website)

    sleep(2)

    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    matches = driver.find_elements('tag name', 'tr')

    date = []
    home_team = []
    score = []
    away_team = []

    for match in matches:
        date.append(match.find_element('xpath', './td[1]').text)
        home_team.append(match.find_element('xpath', './td[2]').text)
        score.append(match.find_element('xpath', './td[3]').text)
        away_team.append(match.find_element('xpath', './td[4]').text)

        print(match.find_element('xpath', './td[4]').text)


        

    while True:
        sleep(5)
        pass

website = 'https://www.adamchoi.co.uk/overs/detailed'  
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'

launchBrowser(website = website, webdriver_path = path)