import os, requests, dotenv

dotenv.load_dotenv()

flight_token = os.getenv('FLIGHT_TOKEN')
flight_url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
flight_url_offers = "https://test.api.amadeus.com/v2/shopping/flight-offers"
flight_headers = {
    "Authorization": f"Bearer {flight_token}"
}

class FlightSearch:
    def __init__(self):
        self.url = flight_url
        self.flight_url_offers = flight_url_offers
        self.headers = flight_headers
        self.token = self.get_new_token()
        self.flight_data = []
    
    def get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        body = {
            "grant_type": "client_credentials",
            "client_id": os.getenv('FLIGHT_API_KEY'),
            "client_secret": os.getenv('FLIGHT_API_SECRET')
        }
        
        try:
            response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=body, headers=headers)
            response.raise_for_status()
            print(f"Your token expires in {response.json()['expires_in']} seconds")
            return response.json()['access_token']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching new token: {e}")
            return None
        
        
    
    def get_iata_codes_from_city(self, city_name):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(self.url + f"?keyword={city_name}&max=3", headers=self.headers)
            response.raise_for_status()
            flight_data = response.json()
            self.flight_data = flight_data['data'][0]
            if self.flight_data['name'].lower() == city_name.lower():
                return self.flight_data['iataCode']
            
            print(f"No IATA code found for {city_name}")
            return ""
        except requests.exceptions.RequestException as e:
            print(f"Error fetching flight data: {e}")
            return ""
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        if not self.token:
            print("No valid token available.")
            return None
        
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "INR",
            "max": "3"
        }
        
        try:
            response = requests.get(self.flight_url_offers, headers=self.headers, params=params)
            response.raise_for_status()
            flight_data = response.json()
            return flight_data
        except requests.exceptions.RequestException as e:
            print(f"Error searching flights: {e}")
            return None