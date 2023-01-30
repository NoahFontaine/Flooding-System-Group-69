# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
  list1 = []
  for station in staions:
    distance = haversine(station.coord, p)
    list1.append[tuple(station, distance)]
  list1.sorted_by_key
  return list1
  
  
