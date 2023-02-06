from floodsystem.geo import stations_within_radius, rivers_by_station_number, stations_by_distance, stations_by_river, rivers_with_station
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


"""Test the function stations_by_distance()"""

def test_stations_by_distance():
    test = stations_by_distance(station_list, (0,0))

    # Test that haversine returns the correct values, and that the return list is sorted correctly

    assert test[0][1] == (0.0)
    assert test[1][1] == (157.2495984740402)
    assert test[2][1] == (11880.582746995915)
    assert test[0][0] == "Label"
    assert test[1][0] == "Label1"
    assert test[2][0] == "Label2"

"""Test the function stations_within_radius()"""

def test_stations_within_radius():
    for i in range(0,200):
        test = stations_within_radius(station_list, (0,0), i)
        # Test that the maximum radius input has the correct effect on the results, and test contains 'Label' or 'Label1'

        if i == 150:
            assert len(test) == 1
            assert 'Label' in test
        if i == 200:
            assert len(test) == 2
            assert 'Label1' in test

print(test_stations_within_radius()) # Should return 'None'

"""Test the function rivers_with_station()"""

def test_rivers_with_station():
    test = rivers_with_station(station_list)
    test_list = list(test)

    # Test that the return set does not have any duplicate entries, and has the correct length

    for i in range(len(test_list)-1):
        assert test_list[i] != test_list[i+1]
    assert len(test_list) == 2

"""Test the function stations_by_river()"""

def test_stations_by_river():
    test = stations_by_river(station_list)

    # Test that function maps the correct keys to the correct station labels

    assert test["River"][0] == "Label"
    assert test["River"][0] == label
    assert len(test["River1"]) == 2

"""Test the function rivers_by_station_number()"""

def test_rivers_by_station_number():
    test = rivers_by_station_number(station_list, 1)

    # Test that the function is the correct length and contains the correct River 1

    assert len(test) == 1
    assert test[0][1] == 2
    assert "River1" in test[0]
    

print(test_stations_by_distance()) # Should return 'None'
print(test_rivers_with_station()) # Should return 'None'
print(test_stations_by_river()) # Should return 'None'
print(test_rivers_by_station_number()) # Should return 'None'