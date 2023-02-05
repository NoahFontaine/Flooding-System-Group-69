from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

if __name__ == "__main__":
  print("*** Task 1D: CUED Part IA Flood Warning System ***")

  x = rivers_with_station(build_station_list()) 
  print(len(x)) # number of rivers with at least one moniroting system
  sorted(x)
  print(x[:10]) # first 10 rivers in alphabetical order

  # This function prints the names of stations located on the following rivers in alphabetical order
  y = stations_by_river(build_station_list())
  sorted(y)
  print(y['River Aire']) 
  print(y['River Cam'])
  print(y['River Thames'])



