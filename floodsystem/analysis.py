import numpy as np
import matplotlib

from datetime import datetime, timedelta

def polyfit(dates, levels, p):
  x = matplotlib.dates.date2num(dates) # List of all the dates converted as integers
  # Calculates the best fit coefficients with a shift in the x-values of value x[0] to avoid any errors
  a_n = np.polyfit(x - x[0], levels, p)
  # Turns those coefficients into a useable polynomial
  poly = np.poly1d(a_n)

  return poly, x[0]

def trend(station, dates, levels, p=4):

    a_n, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x_axis = np.linspace(x[0], x[-1], 50)
    
    y = (a_n(x_axis - d0))
   
    low = station.typical_range[0]
    high = station.typical_range[1]
  
    slope = np.diff(y)

  # criteria 1. max value + 2. rising or falling trend

    if max(y) >= high and slope[-1]>0:
      return(station.town,"severe")
  
    elif max(y) >=high and slope[-1]<=0:
      return(station.town, "high")
    
    elif high>max(y)>= low:
      return(station.town, "moderate")
    
    elif max(y)<low:
      return(station.town,"low")
  
  


