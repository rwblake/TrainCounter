import json
import matplotlib.pyplot as plt

year     = "2025"
month    = "05"
day      = "19"

with open(f"data/{year}-{month}-{day}/totals.json", "r") as f:
	data = json.load(f)
originators = data["originators"]
terminators = data["terminators"]

total = 0
totals = []
for hour in range(24):
	for minute in range(60):
		time = f"{hour:02d}{minute:02d}"
		if time in originators:
			total += originators[time]
		if time in terminators:
			total -= terminators[time]
		totals.append(total)

plt.plot(totals)
plt.show()