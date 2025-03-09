from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time

print("Only one passenger allowed\n")
print("")
print("Enter the following details:\n")
home = input("Enter aiport code of departure: ")
location = input("Enter airport code of destination: ")
depMonth = input("Edepartue (XX): ")
depDay = input("Enter date of departure (XX): ")
retMonth = input("Enter month of return (XX): ")
retDay = input("Enter date of return (XX): ")

# Example URL
url = 'https://www.kayak.com/flights/' + home + '-' + location + '/2025-' + depMonth + '-' + depDay + '/2025-' + retMonth + '-' + retDay

print(url)

# Create a session
session = requests.Session()

# Set headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',  # Do Not Track Request Header
}

# Send a GET request to the URL with headers
response = session.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the page
print(soup.title.string)