from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import MonitoringStation
import matplotlib.pyplot as plt


# Creating 3 test stations to test the functions

station_id = "ID"
measure_id = "Measure"
label = "Label"
coord = (0,0)
typical_range = (0,1)
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

# Making up the latest level of the stations

station.latest_level = 5.32409849287492
station1.latest_level = 3.3243029423094
station2.latest_level = -1.239845324

# Random sample of dates:

dates = ['27/02/2023', '28/02/2023', '30/01/2023']

# Turning the y-axis into a list

levels = [station.latest_level, station1.latest_level, station2.latest_level]

def test_plot_water_levels():
    test = plot_water_levels(station, dates, levels)
    assert station.name == 'Label'

# Check that the plot matches well with the data in lines 40-42 and line 46
print(test_plot_water_levels())