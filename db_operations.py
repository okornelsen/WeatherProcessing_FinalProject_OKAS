'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses sqlite3 to store the weather data in an SQLite database.
'''

from dbcm import DBCM

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

  def fetch_last(self):
    with DBCM("wpg_weather.sqlite") as cursor:
      cursor.execute("select date from wpg_weather order by DATE(date) desc limit 1")
      return [dict(row) for row in cursor.fetchall()]

