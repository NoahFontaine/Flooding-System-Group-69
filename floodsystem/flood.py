from .station import MonitoringStation
from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    list = []  #Empty list
    for station in stations:
        if station.relative_water_level() != None:
            relative = station.relative_water_level()
            if relative > tol:
                list.append((station.name, station.relative_water_level()))
    return sorted_by_key(list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    list = stations_level_over_threshold(stations, 0)
    list1 = []
    for i in range(N):
        list1.append(list[i][0])
    return list1