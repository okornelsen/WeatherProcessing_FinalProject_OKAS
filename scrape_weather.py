'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This Module uses the Python HTMLParser class to scrape Winnipeg weather data (min, max & mean temperatures)
from the Environment Canada website, from the current date, as far back in time as is available.
'''

from html.parser import HTMLParser
import urllib.request

class WeatherScraper(HTMLParser):
  """
  This class manages the components to scrape the meaniningful weather data from the Environment Canada Website.
  """

  def __init__(self):
    HTMLParser.__init__(self)
    self.stack = list()
    self.daily_temps = dict()
    self.weather = dict()
    self.count_item = 0
    self.count_col = 0
    self.date = ""

  def handle_starttag(self, tag, attrs):
    self.stack.append(tag)
    if tag == "td":
      self.count_col += 1

  def handle_endtag(self, tag):
    if tag == "tr":
      self.count_col = 0
      self.count_item = 0
    while self.stack:
      item = self.stack.pop()
      if item == tag:
        break

  def handle_data(self, data):
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

  def return_dict_as_formatted_list(self):
    for keys,values in self.weather.items():
      print(keys,values)


myparser = WeatherScraper()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2004&Month=10') as response:
  html = str(response.read())

myparser.feed(html)
print(myparser.return_dict_as_formatted_list())