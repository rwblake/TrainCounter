# Number of Trains?
Calculate how many trains are currently in service over a given period on National Rail.

Uses the [RealTimeTrains API](https://www.realtimetrains.co.uk/about/developer/) to get timetable information. You can use [realtimetrains.co.uk/](https://www.realtimetrains.co.uk/) to search for trains and view other real-time information services.

"Trains" refers to passenger services.
A train is counted in a given minute if it is the same time or later than its first deprature time of the origin station, and before its final arrival time at the terminus station.

## Directions for Use

To use the script, first register for an API account at [api.rtt.io](https://api.rtt.io).
Upon successful registration, use the provided API Auth Credentials to set local environment variables:
```bash
export REALTIME_TRAINS_USERNAME="your_username"
export REALTIME_TRAINS_PASSWORD="your_password"
```