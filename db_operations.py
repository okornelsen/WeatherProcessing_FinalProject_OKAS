'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses sqlite3 to store the weather data in an SQLite database.
'''

import urllib.request
from scrape_weather import WeatherScraper
from dbcm import DBCM
from datetime import date
import sqlite3
import pprint

class DBOperations:
  """
  This class manages all the db components needed for the weather data.
  """

  def fetch_data(self, data_to_plot):
    pass

  def collect_data(self):
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

        self.save_data(month_dict[month], month, year)
        month -= 1
      month = 12
      year -= 1

  def save_data(self, data, month, year):
    sql = """insert into wpg_weather (date, location, max_temp, min_temp, mean_temp)values (?,?,?,?,?)"""

    location = "Winnipeg, MB"

    for day, temps in data.items():
      set_data = list()
      set_data.append(str(year) + "-" + str(month) + "-" + str(day))
      set_data.append(location)

      for key, value in temps.items():
        set_data.append(value)

      print(set_data)
      with DBCM("wpg_weather.sqlite") as cursor:
        cursor.execute(sql, set_data)

  def initialize_db(self):
    with DBCM("wpg_weather.sqlite") as cursor:
      cursor.execute("""create table if not exists wpg_weather
                  (id integer primary key autoincrement not null,
                  date text not null,
                  location text not null,
                  max_temp real not null,
                  min_temp real not null,
                  mean_temp real not null);""")

  def purge_data(self):
    with DBCM("wpg_weather.sqlite") as cursor:
          cursor.execute("drop table wpg_weather")

if __name__ = "__main__"
  weather = DBOperations()
  weather.purge_data()
  weather.initialize_db()
  weather.collect_data()
