from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_highest_rel_level(stations, 10)
    y = stations_level_over_threshold(stations, 0)
    list = []
    for i in range(len(x)):
        list.append((x[i], y[i][1]))
    for i in list:
        print(str(i[0]), str(i[1]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()