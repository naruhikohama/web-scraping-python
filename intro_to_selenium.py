from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep

def launchBrowser(website, webdriver_path):
    driver = webdriver.Chrome(webdriver_path)
    driver.get(website)

    sleep(2)

    all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
    all_matches_button.click()

    dropdown = Select(driver.find_element('id', 'country'))
    dropdown.select_by_visible_text('Brazil')

    sleep(3)

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

    df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})

    df.to_csv('football_data.csv', index = False)

    print(df)

    driver.quit()

website = 'https://www.adamchoi.co.uk/overs/detailed'  
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'

launchBrowser(website = website, webdriver_path = path)