# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    ### Task 1F ###
    def typical_range_consistent(self):
        if self.typical_range != None:
            if self.typical_range[0] < self.typical_range[1]:
                return True

        return False
    
    ### Task 2B ###
    def relative_water_level(self):
        # Sets the high and low boundaries of the relative water levels
        if self.typical_range != None:
            high = self.typical_range[1]
            low = self.typical_range[0]
        else:
            return None
        # Computes the difference between the typical high and low
        diff = high - low
        if self.latest_level != None:
            llevel = self.latest_level
        else:
            return None
        # Computes the relative water level
        frac = (llevel - low)/diff
        return frac
        
             
def inconsistent_typical_range_stations(stations):
    list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            list.append(station)
    
    return list
