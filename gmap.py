import requests
import json

def get_location(api_key, phone_number):
    API_KEY="AIzaSyBKtfLGo7BNwYb5pUNih1SqudKa_lm4EoQ"
    phone_number="+918714525286"
    # Google Maps Geocoding API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    
    # Construct the request URL
    params = {
        'address': phone_number,
        'key': api_key
    }
    
    # Make a request to the Google Maps API
    response = requests.get(endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        location_data = response.json()
        
        # Check if any results were returned
        if location_data['results']:
            # Extract the formatted address and location coordinates
            formatted_address = location_data['results'][0]['formatted_address']
            location = location_data['results'][0]['geometry']['location']
            return formatted_address, location
        else:
            return "No location found for this number.", None
    else:
        return "Error fetching data from Google Maps API.", None

# Example usage
if __name__ == "_main_":
    API_KEY = "AIzaSyBKtfLGo7BNwYb5pUNih1SqudKa_lm4EoQ"
    phone_number = "+918714525286"  # Replace with the actual phone number
    address, coordinates = get_location(API_KEY, phone_number)
    
    if coordinates:
        print(f"Address: {address}")
        print(f"Coordinates: Latitude {coordinates['lat']}, Longitude {coordinates['lng']}")
    else:
        print(address)