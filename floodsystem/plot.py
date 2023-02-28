import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit
import numpy as np
import matplotlib

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    # Define plot
    plt.plot(dates, levels, label = "collected data")
    
    # Plot x and y-axis

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)


    # Plot the line of best fit
    a_n, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x_axis = np.linspace(x[0], x[-1], 50)
    
    plt.plot(x_axis, a_n(x_axis - d0), label = "trend line of best fit")

    # Add the typical high and low ranges used for Task2F
    low = station.typical_range[0]
    high = station.typical_range[1]

    # Plots these values
    plt.axhline(low, color = "green", linestyle = "dotted", label = "typical low")
    plt.axhline(high, color = "red", linestyle = "dotted", label = "typical high")

    plt.legend()
    plt.tight_layout()
    plt.show()