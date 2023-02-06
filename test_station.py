# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


# Creating 3 test stations to test the functions

station_id = "ID"
measure_id = "Measure"
label = "Label"
coord = (0,0)
typical_range = (0.1,1.8)
river = "River"
town = "Town"
station = MonitoringStation(station_id, measure_id, label, coord, typical_range, river, town)

station_id1 = "ID1"
measure_id1 = "Measure1"
label1 = "Label1"
coord1 = (1,1)
typical_range1 = (-0.4,5)
river1 = "River1"
town1 = "Town1"
station1 = MonitoringStation(station_id1, measure_id1, label1, coord1, typical_range1, river1, town1)

station_id2 = "ID2"
measure_id2 = "Measure2"
label2 = "Label2"
coord2 = (-14.3,107.4)
typical_range2 = (39,4.3)
river2 = "River1"
town2 = "Town2"
station2 = MonitoringStation(station_id2, measure_id2, label2, coord2, typical_range2, river2, town2)

# Create list of test stations

station_list = [station, station1, station2]

"""Test the function inconsistant_typical_range_stations() and the method typical_range_consistent()"""

def test_inconsistant_typical_range_stations():
    test = inconsistent_typical_range_stations(station_list)

    # Veryfy that only station2 is in test

    assert len(test) == 1
    assert station2 in test

    # Verifying that station and station1 are consistent, whereas station2 isn't

    assert MonitoringStation.typical_range_consistent(station) == True
    assert MonitoringStation.typical_range_consistent(station1) == True
    assert MonitoringStation.typical_range_consistent(station2) == False

print(test_inconsistant_typical_range_stations()) # Should print 'None'