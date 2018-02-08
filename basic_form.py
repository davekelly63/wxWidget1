# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class basic_frame
###########################################################################

class basic_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxWidget Basic Test", pos = wx.DefaultPosition, size = wx.Size( 676,570 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizerLeft = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 30, 2 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 227 )
		self.m_grid1.SetColSize( 1, 87 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Net Name" )
		self.m_grid1.SetColLabelValue( 1, u"Visible" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		self.m_grid1.SetColFormatBool(1)

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizerLeft.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		
		bSizer21.Add( bSizerLeft, 3, wx.EXPAND, 5 )
		
		bSizerRight = wx.BoxSizer( wx.VERTICAL )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizerRight.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( bSizerRight, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.Cancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.Ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Cancel( self, event ):
		event.Skip()
	
	def Ok( self, event ):
		event.Skip()
	

