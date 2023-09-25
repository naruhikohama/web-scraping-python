from selenium import webdriver 

website = 'https://www.adamchoi.co.uk/overs/detailed'  
path = 'C:/Users/Naruhiko/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)