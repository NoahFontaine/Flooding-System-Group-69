# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa

## the followings probably not gonna work ##

from haversine import haversine
from floodsystem.stationdata import build_station_list

list1 = []
def stations_by_distance(stations, p):
  for station in staions:
    distance = haversine(station.coord, p)
    list1.append[tuple(station, distance)]
  list1.sorted_by_key
  return list1
  
  
