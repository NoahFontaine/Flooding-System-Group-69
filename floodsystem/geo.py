# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

### Part of 1B - Stations sorted by distance from coordinate ###

def stations_by_distance(stations, p):
  list1 = []  # Empty List
  for station in stations:
    distance = haversine(station.coord, p)
    x = (station.name, distance) # Defines a new tupple for every station
    list1.append(x) # Adds that tupple to list1
  return sorted_by_key(list1, 1) # Returns sorted list1 by 2nd element (distance)


### Part of 1C - Stations within a specific radius of a center coordinate ###

def stations_within_radius(stations, centre, r):
  if r < 0:
    raise ValueError("r must be a positive integer")
  l = []   # Empty list that will contain the output with all the correct stations
  for station in stations:
    distance = haversine(station.coord, centre) # Computes the distance of the station from the given centre coordinate
    if distance < r:
      l.append(station.name) # Adds the station name of the station if distance < given max radius
  return l  # Returns list of all the stations

### Part of 1D ###
def rivers_with_station(stations):
  rivers = []
  for station in stations:
    rivers.append(station.river)
  return set(rivers) # Returns set of all stations with river

def stations_by_river(stations):
  dict = {}
  for station in stations:
    if station.river not in dict:
      dict[station.river] = [station.name]
    else:
      dict[station.river].append(station.name)
      dict[station.river].sort()

  return dict # Returns dictionary of stations by river
  
  
### Part of 1E ###
def rivers_by_station_number(stations, N):
  if N < 0:
    raise ValueError("N must be a positive integer")
  dict = stations_by_river(stations) # Defines the new dictionary from stations_by_river function
  if N > len(dict):
    raise ValueError("N must be smaller than the number of rivers")
  list = [] # Empty list
  for station in stations:
    list.append((station.river,len(dict[station.river])))
  list2 = set(list) # Removes all duplicates
  list3 = sorted_by_key(list2, 1, reverse=True) # Sorts all duplicates from greatest number to smallest
  list4 = []

  for i in range(N): # Adds x many rivers to the list, as required
    list4.append(list3[i])

  for i in range(len(list3)):
    if list3[i][1] == list4[N-1][1]:
      list4.append(list3[i])
  
  return list4
