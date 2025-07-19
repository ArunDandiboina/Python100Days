import requests, os, dotenv, datetime

dotenv.load_dotenv()

nutri_api_key = os.getenv("NT_API")
nutri_app_id = os.getenv("NT_APP_ID")
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_token = os.getenv("TOKEN")
sheety_url = "https://api.sheety.co/07b5c7402cc2c527a8976e53f4defd34/myWorkouts/workouts"


# Nutritionix API requires an app ID and API key
headers = {
    "x-app-id": nutri_app_id,
    "x-app-key": nutri_api_key,
    "Content-Type": "application/json"
}

text = input("Tell me which exercises you did: ")

payload = {
    "query": text,
}

exercises = []
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    exercises = data.get("exercises", [])
    
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
# for exercise in exercises:
#     date = datetime.datetime.now().strftime("%d/%m/%Y")
#     time = datetime.datetime.now().strftime("%H:%M:%S")
#     name = exercise.get("name")
#     duration = exercise.get("duration_min")
#     calories = exercise.get("nf_calories")
    
#     print(f"{date} {time} {name} {duration} {calories}")

# Get Sheety API 

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

# try:
#     response = requests.get(sheety_url, headers=sheety_headers)
#     response.raise_for_status()
#     sheety_data = response.json()
#     print(sheety_data)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred while fetching Sheety data: {e}")
    
# Post data to Sheety API
for exercise in exercises:
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%X")
    name = exercise.get("name")
    duration = exercise.get("duration_min")
    calories = exercise.get("nf_calories")

    sheety_payload = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name.title(),
            "duration": duration,
            "calories": calories
        }
    }

    try:
        response = requests.post(sheety_url, json=sheety_payload, headers=sheety_headers)
        response.raise_for_status()
        print(f"Successfully added {name} to Sheety.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while posting to Sheety: {e}")