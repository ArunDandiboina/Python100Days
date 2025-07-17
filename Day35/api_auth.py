import requests, os, dotenv

from twilio.rest import Client # type: ignore

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
content_sid = os.getenv("CONTENT_SID")
twilio_whatsapp = os.getenv("TWILIO_WHATSAPP")
my_whatsapp = os.getenv("MY_WHATSAPP")

# LOOK AND UNDERSTAND THE API DOCUMENTATION
# Because every API has different ways to access their data.

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY, 
    "cnt": 4
}

api_url = "https://api.openweathermap.org/data/2.5/forecast"

try:
    response = requests.get(api_url, params=parameters)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    l = data["list"]
    # print(len(l))
    # if rain from 9 to 6 print("Bring an umbrella") id < 700
    for item in l:
        if int(item["weather"][0]["id"]) < 700:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_=twilio_whatsapp,
                body=f"Bring an Umbrella.☂️",
                to=my_whatsapp
            )
            # print("Message sent:", message.sid)
            break
        # dt_obj = dt.datetime.fromtimestamp(item["dt"])
        # temp = item["main"]["temp"]
        # weather = item["weather"][0]["description"]
        # print(f"Time: {dt_obj}, Temperature: {temp}K, Weather: {weather}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")