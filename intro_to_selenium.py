from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def launchBrowser(website, webdriver_path):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(webdriver_path, options=chr_options)
    driver.get(website)

website = 'https://www.adamchoi.co.uk/overs/detailed'  
path = 'C:/Users/Naruhiko/Downloads/chromedriver/chromedriver-win32/chromedriver.exe'

launchBrowser(website = website, webdriver_path = path)