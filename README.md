# Number of Trains?
Calculate how many trains are currently in service at a time on National Rail.

Uses the [RealTimeTrains API](https://www.realtimetrains.co.uk/about/developer/) to get timetable information.

"Trains" refers to passenger services.
A train is counted in a given minute if it is the same time or later than its first deprature time of the origin station, and before its final arrival time at the terminus station.