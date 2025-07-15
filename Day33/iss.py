import requests
import datetime as dt

# params = parmeters in sunrise-sunset API
# parameters = {
#     "lat": 17.387140,
#     "lng": 78.491684,
#     "formatted": 0,
#     "tzid": "Asia/Kolkata"
# }

try:
    response = requests.get("https://api.sunrise-sunset.org/json?lat=17.387140&lng=78.491684&tzid=Asia/Kolkata&formatted=0")
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    # print(data)
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    
    print(f"Sunrise: {sunrise}, Sunset: {sunset}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

sunrise = dt.datetime.fromisoformat(sunrise)
sunset = dt.datetime.fromisoformat(sunset)

# string timezone to datetime object example
# s = "2023-10-23T06:00:00+05:30"
# s = dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")
# print(type(s))
# print(s)

# print(sunrise.hour)
# print(sunset.hour)

if sunrise.hour < dt.datetime.now().hour < sunset.hour:
    print("It's daytime!")
else:
    print("It's nighttime!")