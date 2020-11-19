'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module handles the user to download a full set of weather data, or to update it from a menu of choices.
'''

from db_operations import DBOperations
from scrape_weather import WeatherScraper
from plot_operations import PlotOperations
from pubsub import pub
import urllib.request
from datetime import date
import wx
import logging

class WeatherProcessor:
  """
  This class manages the user interaction to generate plots and update the data.
  """

  def __init__(self):
    """ Initialize classes and variables for db operations, web scraping, plot operations and UI configuration """
    try:
      self.db = DBOperations()
      self.ws = WeatherScraper()
      self.pl = PlotOperations()
      self.last_updated = self.db.fetch_last()[0]["sample_date"] if self.db.is_table_exist() else ""
      self.first_updated = self.db.fetch_first()[0]["sample_date"] if self.db.is_table_exist() else ""

    except Exception as e:
      logging.error(f"weatherprocessor:__init__, {e}")

  def download_data(self):
    """ Clears the database, reinitializes it, then downloads all the data to it. """
    try:
      self.db.purge_data()
      self.db.initialize_db()
      self.collect_data()

    except Exception as e:
      logging.error(f"weatherprocessor:download_data, {e}")

  def update_data(self):
    """ Ensures the database exists then downloads all
        the data up to the most recent date in the database. """
    try:
      self.db.initialize_db()
      self.collect_data()
      self.last_updated = self.db.fetch_last()[0]["sample_date"]

    except Exception as e:
      logging.error(f"weatherprocessor:update_data, {e}")

  def get_box_plot(self, start_year, end_year):
    """ Fetches data within the users inputted range then
        generates a box plot for the mean temperatures of each month. """
    try:
      weather = self.db.fetch_data(start_year,int(end_year) + 1,False)
      self.pl.generate_box_plot(weather, start_year, end_year)

    except Exception as e:
      logging.error(f"weatherprocessor:get_box_plot, {e}")

  def get_line_plot(self, year, month):
    """ User inputs the month and year of the data to be fetched
        then generates a line plot for the daily mean temperatures of that month. """
    try:
      weather = self.db.fetch_data(year,month,True)
      self.pl.generate_line_plot(weather, year, month)

    except Exception as e:
      logging.error(f"weatherprocessor:get_line_plot, {e}")

  def collect_data(self):
    """ This method collects the data by looping through and prepping for save,
        Get the current date and break it down into variables,
        Query db for the latest recorded data by date,
        Call the scraper class to collect necessary data,
        Stop collecting after duplicates are found. """
    try:
      today = date.today()
      year = int(today.strftime("%Y"))
      month = int(today.strftime("%m"))
      year_dict = dict()
      duplicate_month,duplicate_day = False, False
      recent_date = ""

      dates = self.db.fetch_last()
      if len(dates) > 0:
          recent_date = dates[0]["sample_date"]

      while not duplicate_month and not duplicate_day:
        """ Iterates through each year starting with the
            latest and working backwards until duplicate data is found. """
        try:
          month_dict = dict()

          while not duplicate_day and month > 0:
            """ Iterate through each month starting with the latest
                and working backwards until duplicate data is found. """
            try:
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
                  """Iterates through each months data enusring there is not a duplicate in the database."""
                  try:
                    check_date = f"{year}-{month:02d}-{key}"
                    if check_date == recent_date:
                      duplicate_day = True

                      break
                    temp_dict[key] = value

                  except Exception as e:
                    logging.error(f"weatherprocessor:collect_data:loop:loop2:loop3, {e}")

                month_dict[month] = temp_dict
              self.db.save_data(month_dict[month], month, year)
              month -= 1

            except Exception as e:
              logging.error(f"weatherprocessor:collect_data:loop:loop2, {e}")

          pub.sendMessage('update_latest_download', year=str(year))
          month = 12
          year -= 1

        except Exception as e:
          logging.error(f"weatherprocessor:collect_data:loop, {e}")

    except Exception as e:
      logging.error(f"weatherprocessor:collect_data, {e}")


  def get_years_for_dropdown(self, min_year):
    """Retrieves the years for the combo boxes based on a given min_year."""
    try:
      years = []

      if self.db.is_table_exist():

        self.last_updated = self.db.fetch_last()[0]["sample_date"] if self.db.is_table_exist() else ""
        self.first_updated = self.db.fetch_first()[0]["sample_date"] if self.db.is_table_exist() else ""

        if min_year == "":
          firstyear = int(self.first_updated[:4])
        else:
          firstyear = int(min_year)

        lastyear = int(self.last_updated[:4])

        while firstyear <= lastyear:
          """Starting from the first year add each year to the years list."""
          try:
            years.append(str(firstyear))
            firstyear += 1

          except Exception as e:
            logging.error(f"weatherprocessor:get_years_for_dropdown:loop, {e}")

      return years

    except Exception as e:
      logging.error(f"weatherprocessor:get_years_for_dropdown, {e}")


  def get_months_for_dropdown(self, year):
    """Retrieves the months for the month combo box based on the selected year."""
    try:
      months = []

      if self.db.is_table_exist():

        self.first_updated = self.db.fetch_first()[0]["sample_date"] if self.db.is_table_exist() else ""

        if year == "":
          year = int(self.first_updated[:4])

        data = self.db.fetch_months(year)


        for item in data:
          """Goes through the list of returned data"""
          try:
            for value in item.values():
              """Adds each month to a list of months."""
              try:
                months.append(str(value[-2:]))

              except Exception as e:
                logging.error(f"weatherprocessor:get_months_for_dropdown:loop:loop2, {e}")

          except Exception as e:
            logging.error(f"weatherprocessor:get_months_for_dropdown:loop, {e}")

      return months[::-1]

    except Exception as e:
      logging.error(f"weatherprocessor:get_months_for_dropdown, {e}")
