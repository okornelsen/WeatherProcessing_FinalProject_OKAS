from html.parser import HTMLParser
import urllib.request

class WeatherScraper:
  """
  This class uses the Python HTMLParser class to scrape Winnipeg weather data (min, max & mean temperatures)
  from the Environment Canada website, from the current date, as far back in time as is available.
  """