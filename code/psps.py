from datetime import datetime, timedelta
import airportsdata

# Define the start and end dates
start_date_str = "2/13/2025"
end_date_str = "3/13/2025"

airports = airportsdata.load('IATA')
code = "MCO"

if code in airports:
    print("WORKS")
else:
    print("NOPE")

# Convert the date strings to datetime objects
start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

# Initialize an empty list to store the days
days = []
interval = 2
next_date = start_date
# Iterate through the range of dates
current_date = start_date
while current_date <= end_date:
    days.append(current_date.strftime("%m/%d/%Y"))
    next_date = current_date + timedelta(days=interval)
    if (next_date <= end_date):
        print("time:" + current_date.strftime("%Y-%m-%d") + "-----" + next_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)
