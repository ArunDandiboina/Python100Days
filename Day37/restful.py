import requests, os, dotenv
import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
date_str = today.strftime("%Y%m%d")
yesterday_str = yesterday.strftime("%Y%m%d")

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USER")

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

# create a user

# pay_load = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# try:
#     response = requests.post(url=pixela_endpoint, json=pay_load)
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

# https://pixe.la/@arun6dan7

# create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# pay_load = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "ajisai",
#     "timezone": "Asia/Kolkata"
# }

# try:
#     response = requests.post(url=graph_endpoint, json=pay_load, headers=headers)
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")


# create a pixel

pixel_endpoint = f"{graph_endpoint}/graph1"

# pay_load = {
#     "date": "20250714",
#     "quantity": "1"
# }

# try:
#     response = requests.post(url=pixel_endpoint, json=pay_load, headers=headers)
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")


# update a pixel

update_pixel_endpoint = f"{pixel_endpoint}/{date_str}"

pay_load = {
    "quantity": "3"
}

try:
    response = requests.put(url=update_pixel_endpoint, json=pay_load, headers=headers)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


# delete a pixel

delete_pixel_endpoint = f"{pixel_endpoint}/{date_str}"

# try:
#     response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")