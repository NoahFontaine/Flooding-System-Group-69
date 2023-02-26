
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def f():
    stations = build_station_list()
    update_water_levels(stations)
    # Computes all the stations and the relative water level that have a relative level above 0.8
    x = stations_level_over_threshold(stations, 0.8)
    for i in x:
        # Prints that list in the required way
        print(str(i[0]), str(i[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    f()