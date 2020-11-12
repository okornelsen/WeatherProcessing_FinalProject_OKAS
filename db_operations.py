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

  def fetch_data(self, start, end, is_month):
    """ This function fetchs the range of data from the db as requested by the user. """

    with DBCM("wpg_weather.sqlite") as cursor:
      if is_month:
        start_date = str(start) + "-" + str(end) + "-" + "01"
        end_date = str(start) + "-" + str(end) + "-" + "31"
      else:
        start_date = str(start)
        end_date = str(end)

      cursor.execute("select * from wpg_weather where date between '" + start_date + "' and '" + end_date + "'")
      return [dict(row) for row in cursor.fetchall()]

  def collect_data(self):

    """ This method collects the data by looping through and prepping for save,
        Get the current date and break it down into variables,
        Query db for the latest recorded data by date,
        Call the scraper class to collect necessary data,
        Stop collecting after duplicates are found. """

    myparser = WeatherScraper()
    today = date.today()
    year = int(today.strftime("%Y")) - 23
    month = int(today.strftime("%m"))
    year_dict = dict()
    duplicate = False
    recent_date = "0-0-0"

    with DBCM("wpg_weather.sqlite") as cursor:
      cursor.execute("select date from wpg_weather order by DATE(date) desc limit 1")
      dates =[dict(row) for row in cursor.fetchall()]

      if len(dates) > 0:
        recent_date = dates[0]["date"]

    while not duplicate:
      """ Iterates through each year starting with the
          latest and working backwards until duplicate data is found. """

      month_dict = dict()

      while month > 0:
        """ Iterate through each month starting with the latest
            and working backwards until duplicate data is found. """

        url = myparser.get_url(year, month)

        with urllib.request.urlopen(url) as response:
          html = str(response.read())

        myparser.feed(html)
        month_dict[month] = myparser.return_dict()

        if month + 1 in month_dict.keys() and month_dict[month] == month_dict[month + 1]:
          """Checks if month is the same as the prior month. Used for download_data """
          month_dict.popitem()
          duplicate = True
          break

        if recent_date[-2:] in month_dict[month].keys() and str(year) + "-" + str(month) == recent_date[:-3]:
          """ Checks if day is the same as the prior day. Used for update_data """
          duplicate = True
          break

        self.save_data(month_dict[month], month, year)
        month -= 1

      month = 12
      year -= 1

  def save_data(self, data, month, year):
    """ This method is used to store the data that is collected into the db """

    sql = """insert into wpg_weather (date, location, max_temp, min_temp, mean_temp)values (?,?,?,?,?)"""
    location = "Winnipeg, MB"

    for day, temps in data.items():
      """ Iterates through each day in data adding that days data to a list. """

      set_data = list()
      set_data.append(str(year) + "-" + str(month) + "-" + str(day))
      set_data.append(location)

      for key, value in temps.items():
        """ Iterates through the days data adding it to a list that is used with the insert statement. """

        set_data.append(value)

      with DBCM("wpg_weather.sqlite") as cursor:
        cursor.execute(sql, set_data)

  def initialize_db(self):
    """ This method is used to initialize the db """

    with DBCM("wpg_weather.sqlite") as cursor:
      cursor.execute("""create table if not exists wpg_weather
                  (id integer primary key autoincrement not null,
                  date text not null,
                  location text not null,
                  max_temp real not null,
                  min_temp real not null,
                  mean_temp real not null);""")

  def purge_data(self):
    """ This method is used to purge the table in the database """

    with DBCM("wpg_weather.sqlite") as cursor:
          cursor.execute("drop table wpg_weather")
