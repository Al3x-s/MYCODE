import requests
from geopy.geocoders import Nominatim
from datetime import datetime

def get_iss_location():
    api_url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(api_url)

    data = response.json()
    timestamp = int(data['timestamp'])
    iss_location = data['iss_position']
    latitude = float(iss_location['latitude'])
    longitude = float(iss_location['longitude'])
        
    geolocator = Nominatim(user_agent="iss_location")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    address = location.address if location else "over an ocean"
    formatted_date = datetime.fromtimestamp(timestamp).strftime('%m/%d/%y')

    print(f"date: {formatted_date}")
    print(f"location: {address}")

get_iss_location()
