from time import sleep
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import progressbar 
import random

# Validate user input
def takeUserInput(parameter):
    while True:
        user_input = input(f"{parameter}: ").upper()
        if len(user_input) != 3:
            print("Please type a valid Airport Code")
        else:
            break
    return user_input

def takeUserDate(parameter):
    today_date = (str(datetime.now()))[:10]
    today_year = int(today_date[0:4])
    today_month = int(today_date[5:7])
    today_day = int(today_date[8:10])

    while True:
        user_input = input(f"{parameter} Date (0000-00-00): ").upper()
        if len(user_input) != 10:
            print("Please type a valid Date")
        else:
            if user_input[4] == "-" and user_input[7] == "-":
                if user_input[0:4].isnumeric() and user_input[5:7].isnumeric() and user_input[8:10]:
                    if int(user_input[0:4]) >= today_year:
                        if int(user_input[5:7]) >= today_month and int(user_input[5:7]) < 12:
                            if (int(user_input[8:10]) >= today_day or int(user_input[5:7]) > today_month) and int(user_input[8:10]) <= 31:
                                break
                            else:
                                print("Please check this day and make sure this date in not in the past or out of range!")
                        else:
                            print("Please check the month and make sure this date in not in the past or out of range!")
                    else:
                        print("Please check the year and make sure this date is not in the past or out of range!")
                else:
                    print("Only integer values are allowed in the dates")
            else:
                print("Please type a date in the format 0000-00-00")
    return user_input

# ASK THE USER WHERE THEY WANT TO FLY
print("\n=================================================================================")
print("=================================================================================\n")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
user_agent_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
chrome_options.add_argument(f"user-agent={user_agent_string}")
driver = webdriver.Chrome(options=chrome_options)

URL = 'https://www.kayak.com/flights/MCO/LAX/2025-05-01/2025-05-3/'
sleep(random.random())
driver.get(URL)

#wait = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "nrc6-inner")))
webContent = BeautifulSoup(driver.page_source, "html.parser")
informationAll = webContent.find_all("div", class_="nrc6-inner")
if informationAll:
    print("WORKS")
else:
    print("NOPE")
driver.quit()
