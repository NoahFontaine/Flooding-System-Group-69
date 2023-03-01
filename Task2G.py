from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import trend
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

import datetime
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    # 5 most at risk stations
    z = stations_highest_rel_level(stations, 5)
   
    list1 = []

    # 2 days for assessment
    dt=2

    for station in stations:
        if station.name in z:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            y = trend(station, dates, levels)
            list1.append([y])
    #list of most at risk towns corresponding to the stations
    
    print(list1)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
