# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
  list1 = []  #Empty List
  for station in stations:
    distance = haversine(station.coord, p)
    x = (station.name, distance) # Defines a new tupple for every station
    list1.append(x) # Adds that tupple to list1
  return sorted_by_key(list1, 1) # Returns sorted list1 by 2nd element (distance)
