import requests, os, dotenv

dotenv.load_dotenv()


flight_token = os.getenv('FLIGHT_TOKEN')
flight_url = 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200'
flight_headers = {
    "Authorization": f"Bearer {flight_token}"
}

sheety_token = os.getenv("TOKEN")
sheety_url = "https://api.sheety.co/07b5c7402cc2c527a8976e53f4defd34/flightDeals/prices"
sheet_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

try:
    flight_response = requests.get(flight_url, headers=flight_headers)
    flight_response.raise_for_status()
    flight_data = flight_response.json()
    flight_destinations = flight_data['data']
    print(flight_destinations)
except requests.exceptions.RequestException as e:
    print(f"Error fetching flight data: {e}")