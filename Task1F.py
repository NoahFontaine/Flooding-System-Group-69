from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
list2 = []
list3 = []

list2 = inconsistent_typical_range_stations(stations)

for station in list2:
    list3.append(station.name)

list3.sort
print(list3)

#not sorted yet
