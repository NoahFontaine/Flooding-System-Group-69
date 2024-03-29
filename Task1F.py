from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
  stations = build_station_list()
  list2 = []
  list3 = []

  list2 = inconsistent_typical_range_stations(stations)

  for station in list2:
    list3.append(station.name)

  x = sorted(list3)

  print(x)

if __name__ == "__main__":
  print("*** Task 1F: CUED Part IA Flood Warning System ***")
  run()
