import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit (dates, levels, p):
  x = matplotlib.dates.date2num(dates) # List of all the dates converted as integers
  # Calculates the best fit coefficients with a shift in the x-values of value x[0] to avoid any errors
  a_n = np.polyfit(x - x[0], levels, p)
  # Turns those coefficients into a useable polynomial
  poly = np.poly1d(a_n)

  return poly, x[0]

