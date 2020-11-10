'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses is a context manager for opening the database
'''

import sqlite3

class DBCM:
  """
  This class maanges all components to using a database cursor.
  """

  def __init__(self, _filename, _mode):
    self.db = "wpg_weather.sqlite"

  def __enter__(self):
    self.conn = sqlite3.connect(self.db)
    self.cur = self.conn.cursor()

  def __exit__(self, exc_type, exc_value, exc_trace):
    self.conn.commit()
    self.conn.close()


