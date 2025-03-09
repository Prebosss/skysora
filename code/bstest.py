from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time

# print("Enter the following details:\n")
# home = input("Enter aiport code of departure: ")
# location = input("Enter airport code of destination: ")
# depMonth = input("Month of departue (XX): ")
# depDay = input("Date of departure (XX): ")
# retMonth = input("Month of return (XX): ")
# retDay = input("Date of return (XX): ")

# Example URL
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
# driver = webdriver.Chrome(options=op)

driver = webdriver.Chrome()
# url = 'https://www.kayak.com/flights/' + home + '-' + location + '/2025-' + depMonth + '-' + depDay + '/2025-' + retMonth + '-' + retDay

url = "https://www.kayak.com/flights/ATL-DFW/2025-04-22/2025-04-29"

arr = []
try:
    # Open the webpage
    driver.get(url)

    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Get the page source
    page_source = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    flights = soup.find_all(class_ = 'Fxw9-result-item-container')

    # print(flights.prettify())

    # price = flights.find_all(class_ = 'f8F1-price-text')
    # print(price.text.strip())

    # arrival = flights.find_all(class_ = 'vmXl vmXl-mod-variant-large')
    # print(arrival.text.strip())

    # depart =  flights.find_all(class_ = 'aOlM')
    # print(depart.text.strip())


    # Print the title of the page
    for flight in flights:
        arrival = flight.find(class_ = 'vmXl vmXl-mod-variant-large')
        print(arrival.text.strip())
        depart =  flight.find(class_ = 'aOlM')
        print(depart.text.strip())
        price = flight.find(class_ = 'f8F1-price-text')
        for p in price:
            print(p.text.strip())
        print("\n")
    print(3)
finally:
    # Close the WebDriver
    driver.quit()




# print(url)

# # Create a session
# session = requests.Session()

# # Set headers
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'DNT': '1',  # Do Not Track Request Header
# }

# # Send a GET request to the URL with headers
# response = session.get(url, headers=headers)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Print the title of the page
# print(soup.title.string)