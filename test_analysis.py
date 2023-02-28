from floodsystem.analysis import polyfit
from floodsystem.stationdata import MonitoringStation
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


p = 5

def test_polyfit():
    # Make a random polynomial out of Task2E stations
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_highest_rel_level(stations, 1)
   
    dt = 10
    for station in stations:
        if station.name in list:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    test = polyfit(dates, levels, p)
    
    # Assert that it is indeed a polynomial of degree p, and that test also contains the square distance
    assert len(test) == 2
    assert len(test[0]) == p

print(test_polyfit())