

import os
import json


import pandas as pd
import requests


username = os.environ.get('REALTIME_TRAINS_USERNAME')
password = os.environ.get('REALTIME_TRAINS_PASSWORD')


df = pd.read_csv("uk-railway-stations/stations.csv")
station_CRSs = df["crsCode"].unique()

year     = "2025"
month    = "05"
day      = "19"

for arrivals in [True, False]:
	for station_CRS in station_CRSs:
		print(station_CRS)
		path = f"data/{year}-{month}-{day}"
		if arrivals:
			path += "/arrivals"
		else:
			path += "/departures"
		filename = f"{path}/{station_CRS}.json"

		if not os.path.exists(path):
			os.makedirs(path)
		elif os.path.isfile(filename):
			continue

		endpoint = f"/json/search/{station_CRS}/{year}/{month}/{day}"
		if arrivals:
			endpoint += "/arrivals"
		response = requests.get(
			"https://api.rtt.io/api/v1/" + endpoint,
			auth=(username, password)
		)
		if not response:
			print(endpoint)
			raise Exception(f"Non-success status code: {response.status_code}")

		content = response.json()
		with open(filename, 'w') as f:
			json.dump(content, f)