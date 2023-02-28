from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

# Creating 3 test stations to test the functions

station_id = "ID"
measure_id = "Measure"
label = "Label"
coord = (0,0)
typical_range = (0,0)
river = "River"
town = "Town"
station = MonitoringStation(station_id, measure_id, label, coord, typical_range, river, town)

station_id1 = "ID1"
measure_id1 = "Measure1"
label1 = "Label1"
coord1 = (1,1)
typical_range1 = (-5,5)
river1 = "River1"
town1 = "Town1"
station1 = MonitoringStation(station_id1, measure_id1, label1, coord1, typical_range1, river1, town1)

station_id2 = "ID2"
measure_id2 = "Measure2"
label2 = "Label2"
coord2 = (-14.3,107.4)
typical_range2 = (-3.9,4.3)
river2 = "River1"
town2 = "Town2"
station2 = MonitoringStation(station_id2, measure_id2, label2, coord2, typical_range2, river2, town2)

# Create list of test stations

station_list = [station, station1, station2]

"""Test the function stations_level_over_threshold()"""

def test_stations_level_over_threshold():
    test = stations_level_over_threshold(station_list, 0.4)



"""Test the function stations_highest_rel_level()"""

def test_stations_highest_rel_level():
    test = stations_highest_rel_level(station_list, 1)


#test_stations_level_over_threshold()
#test_stations_highest_rel_level()