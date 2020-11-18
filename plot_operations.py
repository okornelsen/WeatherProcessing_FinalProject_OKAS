'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses Pythons matplotlib to create a basic boxplot or line plot of mean temperatures
in a date range (year to year, ex. 2000 to 2020) supplied by the user.
For the line plot the user specifies the year and month to be used.
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import locale
from db_operations import DBOperations

class PlotOperations:
  """
  This class manages all the components required to plot the temperature data.
  """

  def generate_box_plot(self, weather, start_year, end_year):
    """ This function creates a box plot based on the user input """

    if len(weather) > 0:

      fig, ax = plt.subplots()
      fig.canvas.set_window_title(f"Weather Processor: {start_year}-{end_year}")
      ax.set_title(f"{start_year}-{end_year}")
      plt.ylabel('Mean Temperature')
      plt.xlabel('Month')

      january, february, march, april, may, june, july, august, september, october, november, december = [],[],[],[],[],[],[],[],[],[],[],[]

      for row in weather:
        """ Iterates through months in year to append into lists used to plot with. """

        if row["mean_temp"] != "N/A":
          month = int(row['date'][5:7].replace("-",""))
          if month == 1: january.append(row["mean_temp"])
          elif month == 2: february.append(row["mean_temp"])
          elif month == 3: march.append(row["mean_temp"])
          elif month == 4: april.append(row["mean_temp"])
          elif month == 5: may.append(row["mean_temp"])
          elif month == 6: june.append(row["mean_temp"])
          elif month == 7: july.append(row["mean_temp"])
          elif month == 8: august.append(row["mean_temp"])
          elif month == 9: september.append(row["mean_temp"])
          elif month == 10: october.append(row["mean_temp"])
          elif month == 11: november.append(row["mean_temp"])
          elif month == 12: december.append(row["mean_temp"])

      data = [january, february, march, april, may, june, july, august, september, october, november, december]
      plt.boxplot(data)
      plt.show()

  def generate_line_plot(self, weather, year, month):
    """ This function creates a line plot based on the user input. """

    if len(weather) > 0:
      day_format = mdates.DateFormatter('%d')
      locale.setlocale(locale.LC_ALL, 'en-CA.utf8')
      date_as_date = datetime.strptime(year+ "-" + month, "%Y-%m")

      fig, ax = plt.subplots()
      fig.canvas.set_window_title(f"Weather Processor: {date_as_date.strftime('%B, %Y')}")
      ax.xaxis.set_major_formatter(day_format)
      plt.ylabel('Mean Temperature')
      plt.xlabel('Day')

      ax.set_title(date_as_date.strftime("%B, %Y"))

      mean_temps = []
      dates = []
      previous_temp = ""

      for row in weather:
        """ Iterates through days in month and appends into lists used to plot with. """

        mean_temp = row["mean_temp"]
        dates.append(row["date"])

        if mean_temp != "N/A":
          mean_temps.append(mean_temp)
          previous_temp = mean_temp
        else:
          mean_temps.append(previous_temp)

      plt.plot(dates, mean_temps)
      plt.show()
