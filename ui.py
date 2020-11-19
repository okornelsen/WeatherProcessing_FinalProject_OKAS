from frm_main import frmMain
from weather_processor import WeatherProcessor
from pubsub import pub
import logging

class UI(frmMain):
  """Overrides the base form with additional functionality."""

  def __init__(self):
    """Initializes the form setting values for widgets."""
    try:
      frmMain.__init__(self, None)
      self.wp = WeatherProcessor()
      pub.subscribe(self.change_accessibility, 'change_accessibility')

      self.populate_cbo()

      self.txtLatestUpload.SetValue(self.wp.last_updated)

    except Exception as e:
      logging.error(f"ui:__init__, {e}")

  def btnBoxOnButtonClick( self, event ):
    """Generates the box plot giving it the values of the start and end year combo boxes."""
    try:
      self.wp.get_box_plot(self.cboBoxStart.GetStringSelection(), self.cboBoxEnd.GetStringSelection())

    except Exception as e:
      logging.error(f"ui:btnBoxOnButtonClick, {e}")

  def cboBoxStartOnChoice( self, event ):
    """When the choice for start year changes update the end year dropdown to start from the selected start year."""
    try:
      self.cboBoxEnd.Clear()
      self.cboBoxEnd.AppendItems(self.wp.get_years_for_dropdown(self.cboBoxStart.GetStringSelection()))
      self.cboBoxEnd.SetSelection( 0 )

    except Exception as e:
      logging.error(f"ui:cboBoxStartOnChoice, {e}")

  def btnLineOnButtonClick( self, event ):
    """Generate the line plot using the year and month selected by the user."""
    try:
      self.wp.get_line_plot(self.cboLineYear.GetStringSelection(), self.cboLineMonth.GetStringSelection())

    except Exception as e:
      logging.error(f"ui:btnLineOnButtonClick, {e}")


  def cboLineYearOnChoice( self, event ):
    """When the year choice changes update the months dropdown to display the appropriate months"""
    try:
      self.cboLineMonth.Clear()
      self.cboLineMonth.AppendItems(self.wp.get_months_for_dropdown(self.cboLineYear.GetStringSelection()))
      self.cboLineMonth.SetSelection( 0 )

    except Exception as e:
      logging.error(f"ui:cboLineYearOnChoice, {e}")

  def btnDownloadOnButtonClick( self, event ):
    """Downloads the weather data, and sets up a subscription to update the textbox."""
    try:
      self.txtLatestDownload.AppendText("Downloading...")
      pub.subscribe(self.update_latest_download, 'update_latest_download')
      self.wp.download_data()
      self.txtLatestDownload.Clear()
      self.txtLatestDownload.AppendText("Complete!")
      self.populate_cbo()

    except Exception as e:
      logging.error(f"ui:btnDownloadOnButtonClick, {e}")

  def btnUpdateOnButtonClick( self, event ):
    """ Updates the weather data with any missing data.
        Updates the the texbox to display the most recent date added to the data."""
    try:
      self.wp.update_data()
      self.txtLatestUpload.SetValue(self.wp.last_updated)
      self.populate_cbo()

    except Exception as e:
      logging.error(f"ui:btnUpdateOnButtonClick, {e}")

  def update_latest_download(self, year):
    """Sets the textbox to display the most recent Year downloaded."""
    try:
      self.txtLatestDownload.Clear()
      self.txtLatestDownload.AppendText(year)

    except Exception as e:
      logging.error(f"ui:update_latest_download, {e}")

  def change_accessibility(self, enabled):
    """ """
    try:
      self.btnBox.Enable(enabled)
      self.btnLine.Enable(enabled)
      self.btnUpdate.Enable(enabled)

    except Exception as e:
      logging.error(f"ui:change_accessibility, {e}")

  def populate_cbo(self):
    """Populates the combo boxes"""
    try:
      self.cboBoxStart.Clear()
      self.cboBoxEnd.Clear()
      self.cboLineYear.Clear()
      self.cboLineMonth.Clear()

      self.cboBoxStart.AppendItems(self.wp.get_years_for_dropdown(""))
      self.cboBoxEnd.AppendItems(self.wp.get_years_for_dropdown(self.cboBoxStart.GetStringSelection()))
      self.cboBoxStart.SetSelection( 0 )
      self.cboBoxEnd.SetSelection( 0 )

      self.cboLineYear.AppendItems(self.wp.get_years_for_dropdown(""))
      self.cboLineMonth.AppendItems(self.wp.get_months_for_dropdown(self.cboLineYear.GetStringSelection()))
      self.cboLineYear.SetSelection( 0 )
      self.cboLineMonth.SetSelection( 0 )

    except Exception as e:
      logging.error(f"ui:populate_cbo, {e}")

