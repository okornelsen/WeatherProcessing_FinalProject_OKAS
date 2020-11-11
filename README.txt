Class Project – Weather Processing App

This project will be marked out of 100 points, and is worth 40% of your final grade.
Develop an application with the following features:

------------------------------------------------ Part 1 – Scraping ------------------------------------------------

1. Create a scrape_weather.py module with a WeatherScraper class inside.

2. Use the Python HTMLParser class to scrape Winnipeg weather data (min, max & mean temperatures) from the
    Environment Canada website, from the current date, as far back in time as is available.
  Link: https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=1900&Month=5

3. Your code must automatically detect when no more weather data is available for scraping. In other words, you
    are not allowed to hard code the last available date into your program. You are also not allowed to fetch
    the last date from any dropdown menus on the site.

4. All scraping code should be self-contained inside the WeatherScraper class. There should be no scraping code
    anywhere else in the program.

#Input#   The starting URL to scrape, encoded with today’s date.
#Output#  A dictionary of dictionaries. For example:
          ◦ daily_temps = {“Max”: 12.0, “Min”: 5.6, “Mean”: 7.1}
          ◦ weather = {“2018-06-01”: daily_temps, “2018-06-02”: daily_temps}


------------------------------------------------ Part 2 - Database ------------------------------------------------

1. Create a db_operations.py module with a DBOperations class inside.

2. Use the Python sqlite3 module to store the weather data in an SQLite database in the specified format. SQL
    queries to create and query the DB can be provided if required. The DB format for your reference:

    ◦ id -> integer, primary key, autoincrement
    ◦ sample_date -> text
    ◦ location -> text
    ◦ min_temp -> real
    ◦ max_temp -> real
    ◦ avg_temp -> real

3. Create a method called fetch_data that will return the requested data for plotting.

4. Create a method called save_data that will save new data to the DB, if it doesn’t already exist,

5. Create a method called initialize_db to initialize the DB if it doesn’t already exist.

6. Create a method called purge_data to purge all the data from the DB for when the program fetches all new weather data.

7. Create a context manager called DBCM to manage the database connections.

8. All database operation should be self contained in the DBOperations class.

#Input#   Dictionary from WeatherScraper class.
#Output#  A rows tuple containing DB records.


------------------------------------------------ Part 3 - Plotting ------------------------------------------------

1. Create a plot_operations.py module with a PlotOperations class inside.

2. Use Python matplotlib to create a basic boxplot of mean temperatures in a date range (year to year, ex. 2000 to 2020) supplied by the user:
    Link: ◦ https://matplotlib.org/examples/pylab_examples/boxplot_demo.html

3. In addition to the above box plot, display a line plot of a particular months mean temperature data,
    based on user input. For example, display all the daily mean temperatures from January 2020,
    with the x axis being the day, and the y axis being temperature.
    Link: ◦ https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glrtutorials-introductory-pyplot-py

4. All plotting code should be self contained in the PlotOperations class. There should be no plotting code anywhere else in the program.

#Input#   Be creative. One way is a dictionary of lists. For example:
          ◦ weather_data = {1: [1.1, 5.5, 6.2, 7.1], 2: [8.1, 5.4, 9.6, 4.7]}
          ◦ The dictionary key is the month: January = 1, February = 2 etc...
          ◦ The data is all the mean temperatures for each day of that month, for every year desired (box plot), or just for a specific year (line plot).
          ◦ You’ll need to do some data shuffling and organizing for this step to put the data in a format ready for plotting.
#Output#  A boxplot displaying one box per month, so it shows all 12 months of the year on one plot. Labels are automatically created from user input.


------------------------------------------------ Part 4 – User Interaction ------------------------------------------------

1. Create a weather_processor.py module with a WeatherProcessor class inside.

2. When the program starts, present the user with a menu of choices.

3. Allow the user to download a full set of weather data, or to update it.
    ◦ When updating, the program should check today’s date and the latest date of weather available in the DB,
      and download what’s missing between those two points, without duplicating any data.

4. Allow the user to enter a year range of interest (from year, to year) to generate the box plot.

5. Allow the user to enter a month and a year to generate the line plot.

6. Use this class to launch and manage all the other tasks.

7. All user interaction should be self contained in the WeatherProcessor class.

#Input#   User supplies input.
#Output#  Call the correct class methods to accomplish the tasks.


------------------------------------------------ Part 5 - Packaging ------------------------------------------------

1. Create a Windows package installer using Inno Setup, that allows a user to install your weather app on a Windows 10 computer.

2. Include your own icon logo and license agreement as part of the installation process.

#Input#   Binary distribution created with the Python pyinstaller module.
#Output#  Standalone exe installer package for Windows 10, clearly labeled and located so it’s easy to find.
          Don’t submit your entire exe build folder please.


------------------------------------------------ Part 6 – Additional Requirements ------------------------------------------------

1. Code must adhere to the PEP8 standard, and will be checked with pytest.
  ◦ To install pytest: pip install pytest pytest-pep8
  ◦ To use pytest: py.test --pep8 mypythonfile.py

2. Code must be documented well for easy review and grading. At minimum:
  ◦ Module level docstring
  ◦ Class level docstring
  ◦ Function/method level docstring

3. Every function/method needs to implement error handling.
4. Errors should be logged to a log file using the python logging module.
5. Code should pass the provided unittest.


------------------------------------------------ Part 7 – Bonus ------------------------------------------------

1. Create a nice user interface with wxPython for all user interaction.

2. Label and align everything properly so it looks nice.

3. The widgets should scale properly when the window is resized.

4. You should be proud to show this to an employer. In other words, it should not be half-baked.

5. The matplotlib charts can open in their own window, they don’t need to be integrated into the UI.