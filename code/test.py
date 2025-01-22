from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver (if it's not in your PATH, you might need to specify the location)
# e.g., "/usr/local/bin/chromedriver" or "/opt/homebrew/bin/chromedriver" depending on installation
# If chromedriver is in your PATH, no need to specify the path here
driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
print(driver.title)
search = driver.find_element(By.NAME, "search_query")
search.send_keys("selenium tutorial")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
