import wx
from ui import UI
import logging

logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("Running: ")

try:
  if __name__ == "__main__":
    app = wx.App()
    frm = UI()
    frm.Show()
    app.MainLoop()

except Exception as e:
  logging.error(f"main_ui, {e}")
