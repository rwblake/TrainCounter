import json
from collections import defaultdict

with open('response.json', 'r') as f:
	content = json.load(f)

station_tiploc = content["location"]["tiploc"]
services = content["services"]

originators = defaultdict(int)
terminators = defaultdict(int)

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

get_originators(services, station_tiploc, originators)
print(originators)