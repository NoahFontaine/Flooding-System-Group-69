from .station import MonitoringStation
from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    list = []
    for station in stations:
        if station.relative_water_level() != None:
            relative = station.relative_water_level()
            print('Hi')
            if relative > tol:
                x = (station.name, station.relative_water_level)
                list.append(x)
    #return sorted_by_key(list, 1, reverse=True)
        return station.relative_water_level()