""""Demonstration program for Task 1C"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key  # noqa


# This program prints the list returned by "stations_within_radius", sorted using the "sorted_by_key" on first entry
print(sorted_by_key(stations_within_radius(build_station_list(), (52.2053, 0.1218), 10), 0))