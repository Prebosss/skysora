import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import pandas as pd
import airportsdata

airports = airportsdata.load('IATA')

def dateChecker(prompt):
    while True:
        date = input(prompt)
        if (datetime.strptime(date, "%m/%d/%Y")) > (datetime.now() + timedelta(days=300)):
            print("Date cannot be more than 300 days in the future")
            continue
        elif (datetime.strptime(date, "%m/%d/%Y") < datetime.now()):
            print("Date cannot be in the past")
            continue
        else:
            try:
                retVal = datetime.strptime(date, "%m/%d/%Y")
                return retVal
            except ValueError:
                print("Incorrect format. Please enter date in MM/DD/YYYY format.")

def airportChecker(prompt):
    while True:
        code = input(prompt)
        if code in airports:
            return code
        else:
            print("Airport code not found. Re-enter airport code.")

def main(): 
    print("Enter the following details:\n")
    home = airportChecker("Enter aiport code of departure: ")
    location = airportChecker("Enter airport code of destination: ")
    depDate = dateChecker("Start Interval (MM/DD/YYYY): ")
    retDate = dateChecker("End Interval (MM/DD/YYYY): ")
    interval = int(input("How many days on the trip (Not Counting Arrival): "))
    while True:
        if (depDate + timedelta(days=interval)) > retDate:
            print("Too many days")
            interval = int(input("How many days on the trip (Not Counting Arrival): "))
        else:
            break
        
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    user_agent_string = ' mozilla/5.0 (windows nt 10.0: win64: x64) applewebkit/537.36 (khtml: like gecko) chrome/58.0.3029.110 safari/537.3'
    options.add_argument(f'user-agent={user_agent_string}')
    driver = webdriver.Chrome(options=options)
    # Initialize an empty list to store the days
    days = []
    array = []
    intDate = depDate
    # Iterate through the range of dates
    current_date = depDate
    while current_date <= retDate:
        days.append(current_date.strftime("%m/%d/%Y"))
        intDate = current_date + timedelta(days=interval)
        if (intDate <= retDate):
            date1 = current_date.strftime("%Y-%m-%d")
            date2 = intDate.strftime("%Y-%m-%d")
            url = "https://www.kayak.com/flights/" + home + "-" + location + "/" + date1 + "/" + date2
            try:
                # Open the webpage
                driver.get(url)

                # Wait for the flight results to load
                retry = 1
                while retry != 0:
                    try:
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "nrc6-inner"))
                        )
                        break
                    except:
                        print("Error on Page")
                        driver.refresh()
                        retry -= 1
                
                # Get the page source
                page_source = driver.page_source

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(page_source, 'html.parser')
                Fxw9 = soup.find(class_ = 'Fxw9')
                if Fxw9:
                    flights = Fxw9.find_all(class_='nrc6-inner')
                    if flights:
                        for flight in flights:

                            #Sets Up all the variables
                            a = flight.find(class_='nrc6-price-section nrc6-mod-multi-fare')
                            b = flight.find_all(class_='VY2U')
                            c = flight.find_all(class_='xdW8')
                            d = flight.find_all(class_='JWEO')

                            #Finds Price
                            if a:
                                p = a.find(class_='f8F1-price-text')
                                price = p.text.strip()
                                e = a.find(class_='ss46-icon-group-wrapper ss46-mod-gap-size-default')
                                if e:
                                    #Carry-On
                                    if e.find(attrs={'aria-label': 'Carry-on bag 1 carry-on bag'}):
                                        carryon = "1 Carry-On Included"
                                    if e.find(attrs={'aria-label': 'Carry-on bag 2 carry-on bag'}):
                                        carryon = "2 Carry-Ons Included"
                                    
                                    if e.find(attrs={'aria-label': 'Carry-on bag No carry-on bags'}):
                                        carryon = "Carry-On Prohibited"
                                    else:
                                        carryon = "Carry-On Fee"

                                    #Checked Bag
                                    if e.find(attrs={'aria-label': 'Checked bag 1 checked bag'}):
                                        checked = "1 Checked Bag Included"
                                    if e.find(attrs={'aria-label': 'Checked bag 2 checked bag'}):
                                        checked = "2 Checked Bags Included"
                                    if e.find(attrs={'aria-label': 'Checked bag No checked bags'}):
                                        checked = "Checked bag Prohibited"
                                    if e.find(attrs={'aria-label': 'Checked bag Checked bag info unavailable'}):
                                        checked = "Checked Bag Info Unavailable"
                                    else:
                                        checked = "Checked Bag Fee"
                                    
                                    #Seats
                                    if e.find(attrs={'aria-label': 'Seat selection Free seat selection'}):
                                        seat = "Free Seat Selection"
                                    if e.find(attrs={'aria-label': 'Seat selection No seat selection'}):
                                        seat = "No Seat Selection"
                                    else:
                                        seat = "Seat Selection Fee"
                                else:
                                    print("ss46-icon-group-wrapper not found.")
                                    carryon = "Error"
                                    checked = "Error"
                                    seat = "Error"
                                    
                                        
                            else:
                                print("nrc6-price-section not found.")

                            #Finds Stops 0-1 & Provider
                            if d:
                                first = True
                                for k in d:
                                    stops = k.find(class_='JWEO-stops-text')
                                    if first:
                                        stops1 = stops.text.strip().rstrip('-')
                                        if stops1 != "nonstop":
                                            stopPlace = k.find(class_='c_cgF c_cgF-mod-variant-default')
                                            if stopPlace:
                                                place1 = stopPlace.text.strip().rstrip('-')
                                        else:
                                            place1 = "None"
                                        first = False
                                    else:
                                        stops2 = stops.text.strip().rstrip('-')
                                        if stops2 != "nonstop":
                                            stopPlace2 = k.find(class_='c_cgF c_cgF-mod-variant-default')
                                            if stopPlace2:
                                                place2 = stopPlace2.text.strip().rstrip('-')
                                        else:
                                            place2 = "None"

                            #Finds Departure and Arrival Times
                            if c:
                                first = True
                                for j in c:
                                    ftime = j.find(class_='vmXl vmXl-mod-variant-default')
                                    if first:
                                        dtime = ftime.text.strip().rstrip('-')
                                        first = False
                                    else:
                                        atime = ftime.text.strip().rstrip('-')
                            
                            #Finds Provider and Flight Time
                            if b:
                                first = True
                                for i in b:
                                    depart = i.find(class_='vmXl vmXl-mod-variant-large')
                                    provider = i.find(class_='c_cgF c_cgF-mod-variant-default')
                                    if first:
                                        dtext = depart.text.strip().rstrip('-')
                                        ptext = provider.text.strip()
                                        first = False
                                    else:
                                        dtext2 = depart.text.strip().rstrip('-')
                                        ptext2 = provider.text.strip()
                                        array.append([date1, date2, price, ptext, stops1, place1, dtext, dtime, ptext2, stops2, place2, dtext2, atime, carryon, checked, seat])
                    else:
                        print("Element with class 'nrc6-inner' not found.")
                else:
                    print("Element with class 'Fxw9' not found.")

            except Exception as e:
                print(e)
                print("Error occurred while scraping the page")
            
        current_date += timedelta(days=1)

    df = pd.DataFrame(array, columns=['Date1', 'Date2', 'Price', 'Provider1', 'Stops1', 'Stop1', 'Flight Time', 'Departure Time', 'Provider2', 'Stops2', 'Stop2', 'Flight Time2', 'Arrival Time', 'Carry-On', 'Checked Bag', 'Seat Selection'])
    df.to_csv('flights.csv')
    minPrice = df['Price'].min()
    minPriceIndex = df['Price'].idxmin()
    print("\n---------------------------------")
    print("Cheapest Flight is: "+ str(minPrice))
    print("Dates: " + df['Date1'][minPriceIndex] + " - " + df['Date2'][minPriceIndex])
    print("Flight Time: " + df['Flight Time'][minPriceIndex] + " - " + df['Flight Time2'][minPriceIndex])
    print("Provider: " + df['Provider1'][minPriceIndex] + " - " + df['Provider2'][minPriceIndex])
    print("Stops: " + df['Stops1'][minPriceIndex] + " - " + df['Stops2'][minPriceIndex])
    print("Stop Locations: " + df['Stop1'][minPriceIndex] + " - " + df['Stop2'][minPriceIndex])
    print("Departure Time: " + df['Departure Time'][minPriceIndex] + " - " + df['Arrival Time'][minPriceIndex])
    print("Carry-On: " + df['Carry-On'][minPriceIndex])
    print("Checked Bag: " + df['Checked Bag'][minPriceIndex])
    print("Seat Selection: " + df['Seat Selection'][minPriceIndex])
    print("------------------------------------\n")
    print("Thank you for using the program")
    driver.quit()

main()