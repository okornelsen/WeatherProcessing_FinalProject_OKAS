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
    self.weather_data = dict()

  def handle_starttag(self, tag, attrs):
    pass

  def handle_endtag(self, tag):
    pass

  def handle_data(self, data):
    pass

  def return_dict_as_formatted_list(self):
    for keys,values in self.weather_data.items():
      print(keys,values)


myparser = WeatherScraper()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=1996&Month=5') as response:
  html = str(response.read())

myparser.feed(html)
print(myparser.return_dict_as_formatted_list())