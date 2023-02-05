from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

if __name__ == "__main__":
  print("*** Task 1D: CUED Part IA Flood Warning System ***")

  s1 = rivers_with_station(build_station_list()) 
  print(len(s1)) # number of rivers with at least one moniroting system
  x = list(s1)
  x.sort()
  print(x[:10]) # first 10 rivers in alphabetical order

  # This function prints the names of stations located on the following rivers in alphabetical order
  y = stations_by_river(build_station_list())
  l1 = y['River Aire']
  l1.sort()
  print(l1) # stations located on River Aire
  l2 = y['River Cam']
  l2.sort()
  print(l2) # stations located on River Cam
  l3 = y['River Thames']
  l3.sort()
  print(l3) # stations located on River Thames



