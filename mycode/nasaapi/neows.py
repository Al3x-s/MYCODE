#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/Users/asanchez/Desktop/mycode/nasaapi/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
#def main():
    ## first grab credentials
 #   nasacreds = returncreds()

    ## update the date below, if you like
 #   startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
 #   neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
 #   neodata = neowrequest.json()

    ## display NASAs NEOW data
 #   print(neodata)


from datetime import datetime, timedelta

def get_dates_between(start_date, end_date):
    date_format = "%Y-%m-%d"
    dates_list = []

    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    dates_list.append(start_date.strftime(date_format))

    delta = timedelta(days=1)

    while start_date < end_date:
        start_date += delta
        dates_list.append(start_date.strftime(date_format))

    return dates_list


def get_data_from_specific_date():
    date_input = input("Enter the date (yyyy-mm-dd): ")
    print(f"Data from {date_input}:")
    nasacreds = returncreds()
    apireq = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=" + date_input + "&" + nasacreds)
    neodata = apireq.json()

    near_earth_objects = neodata["near_earth_objects"][date_input]
    sorted_neos = sorted(near_earth_objects, key=lambda x: x["estimated_diameter"]["meters"]["estimated_diameter_max"], reverse=True)
    for neo in sorted_neos:
        name = neo["name"]
        diameter = neo["estimated_diameter"]["meters"]["estimated_diameter_max"]
        print(f"Name: {name}, Estimated Diameter: {diameter:.2f} meters")

    elem = neodata["element_count"]
    print(f"amout of near earth objects {elem}")


def get_data_from_date_range():
    start_date_input = input("Enter the start date (yyyy-mm-dd): ")
    end_date_input = input("Enter the end date (yyyy-mm-dd): ")
    print(f"Data from {start_date_input} to {end_date_input}:")
    nasacreds = returncreds()
    apireq = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date_input}&end_date={end_date_input}&{nasacreds}")
    neodata = apireq.json()
    print("thisworked part 2")
    datelist = get_dates_between(start_date_input, end_date_input)
    for i in range(len(datelist)):
        apireq = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=" + datelist[i] + "&" + nasacreds)
        neodata = apireq.json()
        print(neodata['near_earth_objects'][datelist[i]][0]['name'])


def main():
    print("Select an option:")
    print("1. Specific date")
    print("2. Date range")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        get_data_from_specific_date()
    elif choice == "2":
        get_data_from_date_range()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



