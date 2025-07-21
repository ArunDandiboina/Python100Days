import requests
import os
import dotenv
dotenv.load_dotenv()

sheety_token = os.getenv("TOKEN")
sheety_url = "https://api.sheety.co/07b5c7402cc2c527a8976e53f4defd34/flightDeals/prices"
sheet_headers = {
    "Authorization": f"Bearer {sheety_token}",
    "Content-Type": "application/json"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.url = sheety_url
        self.headers = sheet_headers
        self.token = sheety_token
    
    def get_destination_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            self.destination_data = response.json()['prices']
            return self.destination_data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching destination data: {e}")
            return None
    
    def update_destination_code(self, city_name, iata_code):
        for destination in self.destination_data:
            if destination['city'].lower() == city_name.lower():
                destination['iataCode'] = iata_code
                update_data = {
                    "price": {
                        "city": destination['city'],
                        "iataCode": iata_code,
                        "lowestPrice": destination['lowestPrice']
                    }
                }
                
                print(f"{self.url}/{destination['id']}")
                response = requests.put(f"{self.url}/{destination['id']}", json=update_data, headers=self.headers)
                response.raise_for_status()
                print(f"Updated {city_name} with IATA code {iata_code}")
      
        
        
    def add_new_city(self, city_name, iata_code, lowest_price):
        new_data = {
            "price": {
                "city": city_name,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }
        try:
            response = requests.post(self.url, json=new_data, headers=self.headers)
            response.raise_for_status()
            print(f"Added new city: {city_name} with IATA code {iata_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error adding new city {city_name}: {e}")