# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 684,392 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 139, 199, 194 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Weather Processor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 28, 70, 90, 90, False, wx.EmptyString ) )

		bSizer6.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.lblBox = wx.StaticText( self, wx.ID_ANY, u"Generate Box Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblBox.Wrap( -1 )
		self.lblBox.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )

		bSizer9.Add( self.lblBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.btnBox = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer17.Add( self.btnBox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblBoxStart = wx.StaticText( self, wx.ID_ANY, u"Start Year:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblBoxStart.Wrap( -1 )
		gSizer23.Add( self.lblBoxStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		cboBoxStartChoices = []
		self.cboBoxStart = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), cboBoxStartChoices, 0 )
		self.cboBoxStart.SetSelection( 0 )
		gSizer23.Add( self.cboBoxStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer17.Add( gSizer23, 1, wx.EXPAND, 5 )

		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblBoxEnd = wx.StaticText( self, wx.ID_ANY, u"End Year:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblBoxEnd.Wrap( -1 )
		gSizer24.Add( self.lblBoxEnd, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cboBoxEndChoices = []
		self.cboBoxEnd = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), cboBoxEndChoices, 0 )
		self.cboBoxEnd.SetSelection( 0 )
		gSizer24.Add( self.cboBoxEnd, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer17.Add( gSizer24, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer17, 1, wx.EXPAND, 5 )


		gSizer9.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.lblLine = wx.StaticText( self, wx.ID_ANY, u"Generate Line Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLine.Wrap( -1 )
		self.lblLine.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )

		bSizer91.Add( self.lblLine, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer171 = wx.BoxSizer( wx.VERTICAL )

		self.btnLine = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer171.Add( self.btnLine, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer231 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblLineYear = wx.StaticText( self, wx.ID_ANY, u"Year:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLineYear.Wrap( -1 )
		gSizer231.Add( self.lblLineYear, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		cboLineYearChoices = []
		self.cboLineYear = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), cboLineYearChoices, 0 )
		self.cboLineYear.SetSelection( 0 )
		gSizer231.Add( self.cboLineYear, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( gSizer231, 1, wx.EXPAND, 5 )

		gSizer241 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblLineMonth = wx.StaticText( self, wx.ID_ANY, u"Month:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLineMonth.Wrap( -1 )
		gSizer241.Add( self.lblLineMonth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cboLineMonthChoices = []
		self.cboLineMonth = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 110,-1 ), cboLineMonthChoices, 0 )
		self.cboLineMonth.SetSelection( 0 )
		gSizer241.Add( self.cboLineMonth, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( gSizer241, 1, wx.EXPAND, 5 )


		bSizer91.Add( bSizer171, 1, wx.EXPAND, 5 )


		gSizer9.Add( bSizer91, 1, wx.EXPAND, 5 )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.lblDownload = wx.StaticText( self, wx.ID_ANY, u"Download All Available Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDownload.Wrap( -1 )
		self.lblDownload.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )

		bSizer24.Add( self.lblDownload, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btnDownload = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer24.Add( self.btnDownload, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer101.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblLatestDownload = wx.StaticText( self, wx.ID_ANY, u"Last Year Downloaded:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLatestDownload.Wrap( -1 )
		gSizer61.Add( self.lblLatestDownload, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.txtLatestDownload = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtLatestDownload.Enable( False )

		gSizer61.Add( self.txtLatestDownload, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer26.Add( gSizer61, 1, wx.EXPAND, 5 )

		self.lblNote = wx.StaticText( self, wx.ID_ANY, u"*Note: This will take a long time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNote.Wrap( -1 )
		self.lblNote.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 91, False, wx.EmptyString ) )

		bSizer26.Add( self.lblNote, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer101.Add( bSizer26, 1, wx.EXPAND, 5 )


		gSizer9.Add( bSizer101, 1, wx.EXPAND, 5 )

		bSizer1011 = wx.BoxSizer( wx.VERTICAL )

		bSizer241 = wx.BoxSizer( wx.VERTICAL )

		self.lblUpdate = wx.StaticText( self, wx.ID_ANY, u"Update Most Recent Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblUpdate.Wrap( -1 )
		self.lblUpdate.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )

		bSizer241.Add( self.lblUpdate, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.btnUpdate = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer241.Add( self.btnUpdate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1011.Add( bSizer241, 1, wx.EXPAND, 5 )

		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblLatestUpdated = wx.StaticText( self, wx.ID_ANY, u"Last Date Updated:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLatestUpdated.Wrap( -1 )
		gSizer6.Add( self.lblLatestUpdated, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txtLatestUpload = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtLatestUpload.Enable( False )

		gSizer6.Add( self.txtLatestUpload, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer261.Add( gSizer6, 1, wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer261.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1011.Add( bSizer261, 1, wx.EXPAND, 5 )


		gSizer9.Add( bSizer1011, 1, wx.EXPAND, 5 )


		bSizer6.Add( gSizer9, 0, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		bSizer34.SetMinSize( wx.Size( -1,20 ) )
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Copyright of Owen Kornelsen and Ashton Schoffner", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer34.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6.Add( bSizer34, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnBox.Bind( wx.EVT_BUTTON, self.btnBoxOnButtonClick )
		self.cboBoxStart.Bind( wx.EVT_CHOICE, self.cboBoxStartOnChoice )
		self.btnLine.Bind( wx.EVT_BUTTON, self.btnLineOnButtonClick )
		self.cboLineYear.Bind( wx.EVT_CHOICE, self.cboLineYearOnChoice )
		self.btnDownload.Bind( wx.EVT_BUTTON, self.btnDownloadOnButtonClick )
		self.btnUpdate.Bind( wx.EVT_BUTTON, self.btnUpdateOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnBoxOnButtonClick( self, event ):
		event.Skip()

	def cboBoxStartOnChoice( self, event ):
		event.Skip()

	def btnLineOnButtonClick( self, event ):
		event.Skip()

	def cboLineYearOnChoice( self, event ):
		event.Skip()

	def btnDownloadOnButtonClick( self, event ):
		event.Skip()

	def btnUpdateOnButtonClick( self, event ):
		event.Skip()


