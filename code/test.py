from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time

# Path to your ChromeDriver (if it's not in your PATH, you might need to specify the location)
# e.g., "/usr/local/bin/chromedriver" or "/opt/homebrew/bin/chromedriver" depending on installation
# If chromedriver is in your PATH, no need to specify the path here

price = 1000000

print("Only one passenger")
print("Enter the following details:\n")
home = input("Enter aiport code of departure: ")
location = input("Enter airport code of destination: ")
depMonth = input("Enter month of departue (XX): ")
depDay = input("Enter date of departure (XX): ")
retMonth = input("Enter month of return (XX): ")
retDay = input("Enter date of return (XX): ")

driver = webdriver.Chrome()
driver.implicitly_wait(2)
try:
    driver.get("https://www.kayak.com/flights/"+home +"-"+location+"/"+"2025-"+depMonth+"-"+depDay+"/2025-"+retMonth+"-"+retDay)
    print(driver.title)
    driver.find_element(By.CLASS_NAME, "c_neb-item-button").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Flight origin input']"))
        )
    except:
        print("Element not found")
        driver.quit()
    search = driver.find_element(By.XPATH, "//*[@aria-label='Flight origin input']")
    search.send_keys(home)

    airport_select = driver.find_element(By.CLASS_NAME, "dX-j-input")
    airport_select.click()


    search = driver.find_element(By.XPATH, "//*[@aria-label='Flight destination input']")
    search.send_keys(location)

    airport_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dX-j-input-wrapper"))
    )
    airport_select.click()


    #April 22, 2025 Prices on this day are below average
    #April 9, 2025 Prices on this day are around average
    #April 6, 2025 Prices on this day are above average


    date_clicker = driver.find_element(By.XPATH, "//*[@aria-label='April 22, 2025 Prices on this day are below average]").click()



    # search.send_keys(Keys.RETURN)
    time.sleep(10)

finally:
    print("hi")
    driver.quit()


