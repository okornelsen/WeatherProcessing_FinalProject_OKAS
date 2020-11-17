'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module handles the user to download a full set of weather data, or to update it from a menu of choices.
'''

from db_operations import DBOperations
from scrape_weather import WeatherScraper
from plot_operations import PlotOperations
import urllib.request
from datetime import date

class WeatherProcessor:
  """
  This class manages the user interaction to generate plots and update the data.
  """

  def __init__(self):
    self.db = DBOperations()
    self.ws = WeatherScraper()
    self.pl = PlotOperations()

  def download_data(self):
    """ Clears the database, reinitializes it, then downloads all the data to it. """

    self.db.purge_data()
    self.db.initialize_db()
    self.collect_data()

  def update_data(self):
    """ Ensures the database exists then downloads all
        the data up to the most recent date in the database. """

    self.db.initialize_db()
    self.collect_data()

  def get_box_plot(self):
    """ Fetches data within the users inputted range then
        generates a box plot for the mean temperatures of each month. """

    weather = self.db.fetch_data(1996,2021,False)
    self.pl.generate_box_plot(weather, 1996, 2020)

  def get_line_plot(self):
    """ User inputs the month and year of the data to be fetched
        then generates a line plot for the daily mean temperatures of that month. """

    weather = self.db.fetch_data(2020,11,True)
    self.pl.generate_line_plot(weather, 2020, 11)

  def collect_data(self):
    """ This method collects the data by looping through and prepping for save,
        Get the current date and break it down into variables,
        Query db for the latest recorded data by date,
        Call the scraper class to collect necessary data,
        Stop collecting after duplicates are found. """

    today = date.today()
    year = int(today.strftime("%Y"))
    month = int(today.strftime("%m"))
    year_dict = dict()
    duplicate_month,duplicate_day = False, False
    recent_date = ""

    dates = self.db.fetch_last()
    if len(dates) > 0:
        recent_date = dates[0]["date"]

    while not duplicate_month and not duplicate_day:
      """ Iterates through each year starting with the
          latest and working backwards until duplicate data is found. """

      month_dict = dict()

      while not duplicate_day and month > 0:
        """ Iterate through each month starting with the latest
            and working backwards until duplicate data is found. """

        url = self.ws.get_url(year, month)

        with urllib.request.urlopen(url) as response:
          html = str(response.read())

        self.ws.feed(html)
        month_dict[month] = self.ws.return_dict()

        if month + 1 in month_dict.keys() and month_dict[month] == month_dict[month + 1]:
          """Checks if month is the same as the prior month. Used for download_data """
          month_dict.popitem()
          duplicate_month = True
          break

        if recent_date != "":
          temp_dict = {}
          for key,value in reversed(month_dict[month].items()):
            if key == recent_date[-2:]:
              duplicate_day = True

              break
            temp_dict[key] = value

          month_dict[month] = temp_dict
          print(month_dict[month])
        self.db.save_data(month_dict[month], month, year)
        month -= 1

      month = 12
      year -= 1

wp = WeatherProcessor()
#wp.update_data()
wp.download_data()
