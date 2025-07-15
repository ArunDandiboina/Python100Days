# API - Application Programming Interface
# It's a set of rules (specs, commands, protocols)
# that allows different software applications to communicate with each other.

# that developers use it to create apps(software) or
# to interact with existing apps.

# types - REST, SOAP, GraphQL, gRPC, etc.
# REST - Representational State Transfer
# REST is an architectural style for designing networked applications.
# It relies on a stateless, client-server, cacheable communications protocol -- HTTP.
# RESTful APIs use HTTP requests to perform CRUD operations
# CRUD - Create, Read, Update, Delete
# No Auth, Basic Auth, API Key, (OAuth, JWT(token based)) Autherization.

# Read Documentation for different APIs clearly.

# api endpoint - URL that you use to access the API.
# api key - a unique identifier used to authenticate requests associated with your account.
# api request - a message sent by a client to an API endpoint.

import requests

try:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response)
    print(type(response))
    data = response.json()
    print(data)
    print(type(data))
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")