

def get_originators(services, station_tiploc, originators):
	"""modify the terminators dictionary with originators for the provided station"""
	for service in services:
		# some services (e.g. those that split) have multiple origins
		for origin in service["locationDetail"]["origin"]:
			# does it originate here?
			if origin["tiploc"] != station_tiploc:
				continue
			# does it not have an arrival time?
			# (check it didn't originate here earlier)
			if "gbttBookedArrival" in service["locationDetail"]:
				continue

			departure_time = service["locationDetail"]["gbttBookedDeparture"]
			originators[departure_time] += 1


def get_terminators(services, station_tiploc, terminators):
	"""modify the terminators dictionary with terminators for the provided station"""
	for service in services:
		# some services (e.g. those that split) have multiple destinations
		for destination in service["locationDetail"]["destination"]:
			# does it terminate here?
			if destination["tiploc"] != station_tiploc:
				continue
			# does it not have a departure time?
			# (check it isn't terminating here later)
			if "gbttBookedDeparture" in service["locationDetail"]:
				continue

			arrival_time = service["locationDetail"]["gbttBookedArrival"]
			terminators[arrival_time] += 1


def main():
	import json
	from collections import defaultdict
	import pandas as pd
	import os

	df = pd.read_csv("uk-railway-stations/stations.csv")
	station_CRSs = df["crsCode"].unique()
	year     = "2025"
	month    = "05"
	day      = "19"

	originators = defaultdict(int)
	terminators = defaultdict(int)
	for arrivals in [True, False]:
		for station_CRS in station_CRSs:
			if arrivals:
				print(station_CRS)
			path = f"data/{year}-{month}-{day}"
			if arrivals:
				path += "/arrivals"
			else:
				path += "/departures"
			filename = f"{path}/{station_CRS}.json"
			if not os.path.isfile(filename):
				continue
			with open(filename, 'r') as f:
				content = json.load(f)
			if "error" in content:
				continue
			station_tiploc = content["location"]["tiploc"]
			services = content["services"]
			if services is None:
				continue

			if arrivals:
				get_terminators(services, station_tiploc, terminators)
			else:
				get_originators(services, station_tiploc, originators)

	data = {"originators": dict(originators), "terminators": dict(terminators)}
	with open(f"data/{year}-{month}-{day}/totals.json", "w") as f:
		json.dump(data, f, indent=2)


if __name__ == "__main__":
	main()

