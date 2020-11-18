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
    self.last_updated = self.db.fetch_last()[0]["date"] if self.db.table_init() else ""
    self.first_updated = self.db.fetch_first()[0]["date"] if self.db.table_init() else ""
    self.last_downloaded = ""


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
    self.last_updated = self.db.fetch_last()[0]["date"]

  def get_box_plot(self, start_year, end_year):
    """ Fetches data within the users inputted range then
        generates a box plot for the mean temperatures of each month. """

    weather = self.db.fetch_data(start_year,int(end_year) + 1,False)
    self.pl.generate_box_plot(weather, start_year, end_year)

  def get_line_plot(self, year, month):
    """ User inputs the month and year of the data to be fetched
        then generates a line plot for the daily mean temperatures of that month. """

    weather = self.db.fetch_data(year,month,True)
    self.pl.generate_line_plot(weather, year, month)

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
            check_date = f"{year}-{month:02d}-{key}"
            if check_date == recent_date:
              duplicate_day = True

              break
            temp_dict[key] = value

          month_dict[month] = temp_dict
        self.db.save_data(month_dict[month], month, year)
        self.last_downloaded = f"{year}-{month}"
        print("Downloading: ", self.last_downloaded)
        month -= 1

      month = 12
      year -= 1

  def get_years_for_dropdown(self, min_year):
    if min_year == "":
      firstyear = int(self.first_updated[:4])
    else:
      firstyear = int(min_year)

    lastyear = int(self.last_updated[:4])
    years = []
    while firstyear <= lastyear:
      years.append(str(firstyear))
      firstyear += 1
    return years

  def get_months_for_dropdown(self, year):
    if year == "":
      year = int(self.first_updated[:4])

    data = self.db.fetch_months(year)
    months = []

    for item in data:
      for value in item.values():
        months.append(str(value[-2:]))
    return months[::-1]
