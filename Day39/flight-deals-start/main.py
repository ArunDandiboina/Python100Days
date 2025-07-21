import datetime, time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


sheety_data_manager = DataManager()
flight_search = FlightSearch()

data = sheety_data_manager.get_destination_data()
origin_city_code = "BLR"  # Example origin city code

# for destination in data:
#     if destination['iataCode'] == '':
#         iata_code = flight_search.get_iata_codes_from_city(destination['city'])
#         if iata_code:
#             sheety_data_manager.update_destination_code(destination['city'], iata_code)

# print(data)

# search for cheap flights
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
two_months_from_today = now + datetime.timedelta(days=2 * 30)


for destination in data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=two_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price == "N/A":
        continue
    print(f"{destination['city']}: Rs {cheapest_flight.price}")
    if cheapest_flight.price < destination['lowestPrice']:
        print(f"Found a cheaper flight to {destination['city']} for Rs {cheapest_flight.price} !")

    # Slowing down requests to avoid rate limit
    time.sleep(2)