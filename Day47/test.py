
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# response = requests.post(
#     'https://api.perplexity.ai/chat/completions',
#     headers={
#         'Authorization': f'Bearer {os.getenv("PERPLEXITY_API_KEY")}',
#         'Content-Type': 'application/json'
#     },
#     json={
#         'model': 'sonar-pro',
#         'messages': [
#             {
#                 'role': 'user',
#                 'content': "What are the major AI developments and announcements from today across the tech industry?"
#             }
#         ]
#     }
# )

# print(response.json())



response = requests.post(
    'https://api.perplexity.ai/chat/completions',
    headers={
        'Authorization': f'Bearer {os.getenv("PERPLEXITY_API_KEY")}',
        'Content-Type': 'application/json'
    },
    json={
        'model': 'sonar',
        'messages': [
            {
                'role': 'user',
                'content': 'Find the top 3 trending AI startups with recent funding. Include company name, funding amount, and focus area.'
            }
        ],
        'response_format': {
            'type': 'json_schema',
            'json_schema': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'startups': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'company_name': {'type': 'string'},
                                    'funding_amount': {'type': 'string'},
                                    'focus_area': {'type': 'string'}
                                },
                                'required': ['company_name', 'funding_amount', 'focus_area']
                            }
                        }
                    },
                    'required': ['startups']
                }
            }
        }
    }
)

# get content from response
content = response.json()['choices'][0]['message']['content']

print(content)