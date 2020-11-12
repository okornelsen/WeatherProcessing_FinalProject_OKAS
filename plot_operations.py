'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses Pythons matplotlib to create a basic boxplot of mean temperatures
in a date range (year to year, ex. 2000 to 2020) supplied by the user.
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from db_operations import DBOperations

class PlotOperations:
  """
  This class manages all the components required to plot the temperature data.
  """

  def generate_box_plot(self, weather_dict, start_year, end_year):
    pass

  def generate_line_plot(self, weather, year, month):

    if len(weather) > 0:
      day_format = mdates.DateFormatter('%d')
      fig, ax = plt.subplots()
      ax.xaxis.set_major_formatter(day_format)
      plt.ylabel('Mean Temperature')
      plt.xlabel('Date')

      date_as_date = datetime.strptime(str(year) + str(month), "%Y%m")
      ax.set_title(date_as_date.strftime("%B, %Y"))

      mean_temps = []
      dates = []
      previous_temp = ""
      for row in weather:
        mean_temp = row["mean_temp"]
        dates.append(row["date"])

        if mean_temp != "N/A":
          mean_temps.append(mean_temp)
          previous_temp = mean_temp
        else:
          mean_temps.append(previous_temp)

      plt.plot(dates, mean_temps)

      plt.show()

