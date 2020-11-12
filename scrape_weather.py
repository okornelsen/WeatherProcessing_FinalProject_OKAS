'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This Module uses the Python HTMLParser class to scrape Winnipeg weather data (min, max & mean temperatures)
from the Environment Canada website, from the current date, as far back in time as is available.
'''

from html.parser import HTMLParser

class WeatherScraper(HTMLParser):
  """
  This class manages the components to scrape the meaniningful weather data from the Environment Canada Website.
  """

  def __init__(self):
    """ Initializes variables,lists and dictionaries needed for scraping. """
    HTMLParser.__init__(self)
    self.stack = list()
    self.daily_temps = dict()
    self.weather = dict()
    self.count_item = 0
    self.count_col = 0
    self.date = ""

  def handle_starttag(self, tag, attrs):
    """ Builds list stack for every tag element we enter into.
        Increases column count to check what column we are inside. """

    self.stack.append(tag)
    if tag == "td":
      self.count_col += 1

  def handle_endtag(self, tag):
    """ Removes latest tag from the list stack when we exit out of a tag element and
        Reset the column and item count on exit. """

    if tag == "tr":
      self.count_col = 0
      self.count_item = 0

    while self.stack:
      """ Loops through and pop off tag until stack is empty and no tags remain unhandled. """

      item = self.stack.pop()
      if item == tag:
        break

  def handle_data(self, data):
    """ Verify we are accessing the right data by way of tag sequence from built up stack.
        Collect the Date from the table header and the daily temperatures from the table data.
        Handle data that are not proper values, such as "E" and "M"
        Insert value into proper dictionary key dependant on the column we are accessing (column count).
        Append daily temperature dictionary into weather dictionary by way of the Date key. """

    if self.stack[-5:] == ["tbody", "tr", "th", "abbr", "a"] or self.stack[-4:] == ["tbody", "tr", "th", "abbr"]:
      if data.isdigit():
        self.date = data

    if self.stack[-3:] == ["tbody", "tr", "td"] or self.stack[-2:] == ["td", "a"] and self.count_col <= 3:

      if data == "M" or data == "\xa0":
        data = "N/A"
      elif data == "E":
        return

      if self.count_item == 0:
        self.daily_temps["Max"] = data
        self.count_item += 1

      elif self.count_item == 1:
        self.daily_temps["Min"] = data
        self.count_item += 1

      elif self.count_item == 2:
        self.daily_temps["Mean"] = data
        self.count_item += 1

        if not self.date in self.weather.keys():
          self.weather[self.date] = self.daily_temps
          self.daily_temps = dict()

  def return_dict(self):
    """ Returns the weather as a dictionary. """

    temp_weather = self.weather
    self.weather = dict()
    return temp_weather

  def return_dict_as_formatted_list(self):
    """ Return the dictionary as a formatted list of key values pairs. """

    for keys,values in self.weather.items():
      """ Iterates through and prints out the keys and values in weather. """
      print(keys,values)

  def get_url(self, year, month):
    """ Retrieves the url used in db operations to collect data. """

    urlstring = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&"
    year_url = "Year=" + str(year)
    month_url = "&Month=" + str(month)
    return urlstring + year_url + month_url