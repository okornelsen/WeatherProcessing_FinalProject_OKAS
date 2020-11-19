'''
Owen Kornelsen & Ashton Schoffner
November 09, 2020
ADEV-3005 Programming in Python

This module uses is a context manager for opening the database
'''

import sqlite3
import logging

class DBCM:
  """
  This class manages all components to using a database cursor.
  """

  def __init__(self, database):
    """ Initializes the database connection. """
    try:
      self._db = database

    except Exception as e:
      logging.error(f"dbcm:__init__, {e}")

  def __enter__(self):
    """ Establishes cursor connection to be used in db_operations. """
    try:
      self.conn = sqlite3.connect(self._db)
      self.conn.row_factory = sqlite3.Row
      self.cursor = self.conn.cursor()
      return self.cursor

    except Exception as e:
      logging.error(f"dbcm:__enter__, {e}")

  def __exit__(self, exc_type, exc_value, exc_trace):
    """ Commits changes to the database and closes the cursor and database connection. """
    try:
      self.conn.commit()
      self.cursor.close()
      self.conn.close()

    except Exception as e:
      logging.error(f"dbcm:__exit__, {e}")
