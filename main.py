import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get('https://www.google.com')


search = browser.find_element(By.NAME, 'q')
search.send_keys('Cristiano Ronaldo')
search.send_keys(Keys.ENTER) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.quit()
