from frm_main import frmMain
from weather_processor import WeatherProcessor

class UI(frmMain):
  def __init__(self):
    frmMain.__init__(self, None)
    self.wp = WeatherProcessor()
    self.txtLatestUpload.SetValue(self.wp.last_updated)
    self.cboBoxStart.AppendItems(self.wp.get_years_for_dropdown(""))
    self.cboBoxEnd.AppendItems(self.wp.get_years_for_dropdown(self.cboBoxStart.GetStringSelection()))
    self.cboBoxStart.SetSelection( 0 )
    self.cboBoxEnd.SetSelection( 0 )

    self.cboLineYear.AppendItems(self.wp.get_years_for_dropdown(""))
    self.cboLineMonth.AppendItems(self.wp.get_months_for_dropdown(self.cboLineYear.GetStringSelection()))
    self.cboLineYear.SetSelection( 0 )
    self.cboLineMonth.SetSelection( 0 )
    #cboBoxStartChoices = []

  def btnBoxOnButtonClick( self, event ):
    self.wp.get_box_plot(self.cboBoxStart.GetStringSelection(), self.cboBoxEnd.GetStringSelection())

  def cboBoxStartOnChoice( self, event ):
    self.cboBoxEnd.Clear()
    self.cboBoxEnd.AppendItems(self.wp.get_years_for_dropdown(self.cboBoxStart.GetStringSelection()))
    self.cboBoxEnd.SetSelection( 0 )

  def btnLineOnButtonClick( self, event ):
    self.wp.get_line_plot(self.cboLineYear.GetStringSelection(), self.cboLineMonth.GetStringSelection())

  def cboLineYearOnChoice( self, event ):
    self.cboLineMonth.Clear()
    self.cboLineMonth.AppendItems(self.wp.get_months_for_dropdown(self.cboLineYear.GetStringSelection()))
    self.cboLineMonth.SetSelection( 0 )

  def btnDownloadOnButtonClick( self, event ):
    print("Downloading...")
    self.wp.download_data()
    print("Done")

  def btnUpdateOnButtonClick( self, event ):
    print("Updating...")
    self.wp.update_data()
    self.txtLatestUpload.SetValue(self.wp.last_updated)
    print("Done")