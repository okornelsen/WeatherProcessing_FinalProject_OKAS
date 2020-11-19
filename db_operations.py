'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses sqlite3 to store the weather data in an SQLite database.
'''

from dbcm import DBCM
from pubsub import pub
import logging

class DBOperations:
  """
  This class manages all the db components needed for the weather data.
  """

  def fetch_data(self, start, end, is_month):
    """ This function fetchs the range of data from the db as requested by the user. """
    try:
      with DBCM("samples.sqlite") as cursor:
        if is_month:
          start_date = f"{str(start)}-{str(end)}-01"
          end_date = f"{str(start)}-{str(end)}-31"
        else:
          start_date = start
          end_date = str(end)

        cursor.execute(f"select sample_date, avg_temp from samples where sample_date between '{start_date}' and '{end_date}' order by DATE(sample_date) asc")
        return [dict(row) for row in cursor.fetchall()]
    except Exception as e:
      logging.error(f"dboperations:fetch_data, {e}")


  def save_data(self, data, month, year):
    """ This method is used to store the data that is collected into the db """
    try:
      sql = """insert into samples (sample_date, location, max_temp, min_temp, avg_temp)values (?,?,?,?,?)"""
      location = "Winnipeg, MB"

      for day, temps in data.items():
        """ Iterates through each day in data adding that days data to a list. """
        try:
          set_data = list()
          set_data.append(f"{str(year)}-{month:02d}-{str(day)}")
          set_data.append(location)

          for key, value in temps.items():
            """ Iterates through the days data adding it to a list that is used with the insert statement. """
            try:
              set_data.append(value)

            except Exception as e:
              logging.error(f"dboperations:fetch_data:loop:2, {e}")

          with DBCM("samples.sqlite") as cursor:
            cursor.execute(sql, set_data)

        except Exception as e:
          logging.error(f"dboperations:fetch_data:loop, {e}")

    except Exception as e:
      logging.error(f"dboperations:save_data, {e}")

  def initialize_db(self):
    """ This method is used to initialize the db """
    try:
      with DBCM("samples.sqlite") as cursor:
        cursor.execute("""create table if not exists samples
                    (id integer primary key autoincrement not null,
                    sample_date text not null,
                    location text not null,
                    max_temp real not null,
                    min_temp real not null,
                    avg_temp real not null);""")

    except Exception as e:
      logging.error(f"dboperations:initialize_db, {e}")

  def purge_data(self):
    """ This method is used to purge the table in the database """
    try:
      if self.is_table_exist():
        with DBCM("samples.sqlite") as cursor:
            cursor.execute("drop table samples")

    except Exception as e:
      logging.error(f"dboperations:purge_data, {e}")

  def fetch_last(self):
    """ This method is used to get the most recent date from the db """
    try:
      with DBCM("samples.sqlite") as cursor:
        cursor.execute("select sample_date from samples order by DATE(sample_date) desc limit 1")
        return [dict(row) for row in cursor.fetchall()]

    except Exception as e:
      logging.error(f"dboperations:fetch_last, {e}")

  def fetch_first(self):
    """ This method is used to get the least recent date from the db """
    try:
      with DBCM("samples.sqlite") as cursor:
        cursor.execute("select sample_date from samples order by DATE(sample_date) asc limit 1")
        return [dict(row) for row in cursor.fetchall()]

    except Exception as e:
      logging.error(f"dboperations:fetch_first, {e}")

  def fetch_months(self, year):
    """ This method is used to return a dictionary of months given in a year of data """
    try:
      with DBCM("samples.sqlite") as cursor:
        cursor.execute(f"select distinct substr(sample_date, 0, 8) from samples where sample_date like '{year}%' order by DATE(sample_date) desc")
        return [dict(row) for row in cursor.fetchall()]

    except Exception as e:
      logging.error(f"dboperations:fetch_months, {e}")

  def is_table_exist(self):
    """ This method is used to check if we have a db table named samples """
    try:
      with DBCM("samples.sqlite") as cursor:
        cursor.execute("select COUNT(*) from sqlite_master where name = 'samples'")
        if cursor.fetchone()[0] == 1:
          pub.sendMessage('change_accessibility', enabled=True)
          return True
        else:
          pub.sendMessage('change_accessibility', enabled=False)
          return False

    except Exception as e:
      logging.error(f"dboperations:is_table_exist, {e}")
