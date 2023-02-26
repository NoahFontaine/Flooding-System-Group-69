from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations) # Updates the water level
    x = stations_highest_rel_level(stations, 10) # Computes the first 10 station names with the highest level
    y = stations_level_over_threshold(stations, 0) # Computes all the relative water levels
    list = []
    for i in range(len(x)):
        list.append((x[i], y[i][1])) # Creates a list with the first 10 station names and the matched water level
    for i in list:
        # Prints in the correct format
        print(str(i[0]), str(i[1]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()