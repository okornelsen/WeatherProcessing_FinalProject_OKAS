from frm_main import frmMain
from weather_processor import WeatherProcessor

class UI(frmMain):
  def __init__(self):
    frmMain.__init__(self, None)
    self.wp = WeatherProcessor()
    self.txtLatestUpload.SetValue(self.wp.last_updated)

  def btnBoxOnButtonClick( self, event ):
    print("Hello World")

  def btnLineOnButtonClick( self, event ):
    event.Skip()

  def btnDownloadOnButtonClick( self, event ):
    print("Downloading...")
    self.wp.download_data()
    print("Done")

  def btnUpdateOnButtonClick( self, event ):
    print("Updating...")
    self.wp.update_data()
    self.txtLatestUpload.SetValue(self.wp.last_updated)
    print("Done")