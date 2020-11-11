'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses sqlite3 to store the weather data in an SQLite database.
'''

import urllib.request
from scrape_weather import WeatherScraper
from datetime import date
import sqlite3
import pprint

class DBOperations:
  """
  This class manages all the db components needed for the weather data.
  """

  def fetch_data(self, data_to_plot):
    pass

  def save_data(self, weather):
    pass

  def initialize_data(self):
    myparser = WeatherScraper()
    today = date.today()
    year = int(today.strftime("%Y"))
    month = int(today.strftime("%m"))
    year_dict = dict()
    duplicate = False

    while not duplicate:
      month_dict = dict()

      while month > 0:
        url = myparser.get_url(year, month)

        with urllib.request.urlopen(url) as response:
          html = str(response.read())

        myparser.feed(html)
        month_dict[month] = myparser.return_dict()

        if month + 1 in month_dict.keys() and month_dict[month] == month_dict[month + 1]:
          month_dict.popitem()
          duplicate = True
          break

        month -= 1

      month = 12
      year_dict[year] = month_dict
      year -= 1

  def purge_data(self):
    pass

weather = DBOperations()
weather.initialize_data()
