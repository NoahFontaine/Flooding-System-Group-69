from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

if __name__ == "__main__":
    print(rivers_by_station_number(build_station_list(), 9))
