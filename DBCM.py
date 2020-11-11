'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses is a context manager for opening the database
'''

import sqlite3

class DBCM:
  """
  This class manages all components to using a database cursor.
  """

  def __init__(self, _db):
    self.db = _db

  def __enter__(self):
    self.conn = sqlite3.connect(self.db)
    self.cursor = self.conn.cursor()
    return self.cursor

  def __exit__(self, exc_type, exc_value, exc_trace):
    self.conn.commit()
    self.cursor.close()
    self.conn.close()


