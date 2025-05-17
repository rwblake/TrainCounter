import requests

import os
import json

username = os.environ.get('REALTIME_TRAINS_USERNAME')
password = os.environ.get('REALTIME_TRAINS_PASSWORD')
endpoint = "/json/search/WOF/2025/05/19"

print(username)
print(password)

response = requests.get(
	"https://api.rtt.io/api/v1/" + endpoint,
	auth=(username, password)
)

content = response.json()
with open('response.json', 'w') as f:
	json.dump(content, f, indent=2)

print(response.status_code)