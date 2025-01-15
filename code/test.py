from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver (if it's not in your PATH, you might need to specify the location)
# e.g., "/usr/local/bin/chromedriver" or "/opt/homebrew/bin/chromedriver" depending on installation
# If chromedriver is in your PATH, no need to specify the path here
driver = webdriver.Chrome()

try:
    # Step 1: Open Google
    driver.get("https://www.google.com")

    # Step 2: Assert that the title contains 'Google'
    assert "Google" in driver.title

    print("Test passed: Google page title is correct.")

    # Step 3: Find the search input field, type a query, and press 'Enter'
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver" + Keys.RETURN)

    # Step 4: Wait a few seconds to let the page load
    time.sleep(2)

    # Step 5: Assert that results show up (checking if results are visible)
    results = driver.find_elements(By.XPATH, "//h3")
    assert len(results) > 0

    print("Test passed: Search results displayed.")

finally:
    # Step 6: Close the browser window
    driver.quit()
