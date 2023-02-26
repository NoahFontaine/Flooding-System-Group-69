
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def f():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_level_over_threshold(stations, 0.8)
    for i in x:
        print(str(i[0]), str(i[1]))

#print(stations_level_over_threshold(build_station_list(), 0.9))
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    f()