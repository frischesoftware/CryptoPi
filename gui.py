# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class GUI_MainFrame
###########################################################################

class GUI_MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MD5 Calculator", pos = wx.DefaultPosition, size = wx.Size( 1063,710 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFrom = wx.StaticText( self.panel1, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFrom.Wrap( -1 )
		bSizer20.Add( self.lblFrom, 0, wx.ALL, 5 )
		
		self.txtContactA = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.txtContactA, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTo = wx.StaticText( self.panel1, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTo.Wrap( -1 )
		bSizer21.Add( self.lblTo, 0, wx.ALL, 5 )
		
		cmbContactBChoices = []
		self.cmbContactB = wx.ComboBox( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cmbContactBChoices, 0 )
		bSizer21.Add( self.cmbContactB, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self.panel1, wx.ID_ANY, u"&Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.panel1, wx.ID_ANY, u"&Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer6, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.textMessageText = wx.richtext.RichTextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer4.Add( self.textMessageText, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self.panel1, wx.ID_ANY, u"text length:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		bSizer321.Add( self.lbl1, 0, wx.ALL, 5 )
		
		self.lblTextLength = wx.StaticText( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTextLength.Wrap( -1 )
		bSizer321.Add( self.lblTextLength, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer321, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnConvertToBinary = wx.Button( self.panel1, wx.ID_ANY, u"Show as Binary", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.btnConvertToBinary, 0, wx.ALL, 5 )
		
		self.textBinaryText = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_NOHIDESEL|wx.TE_READONLY|wx.TE_RICH|wx.TE_WORDWRAP|wx.VSCROLL )
		bSizer51.Add( self.textBinaryText, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnLoadCurrentKey = wx.Button( self.panel1, wx.ID_ANY, u"btnLoadCurrentKey", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer28.Add( self.btnLoadCurrentKey, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.panel1, wx.ID_ANY, u"Next Key File is:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer28.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.textCurrentKey = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer28.Add( self.textCurrentKey, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( self.panel1, wx.ID_ANY, u"max. Message Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		bSizer28.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.textMaxMessageLength = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer28.Add( self.textMaxMessageLength, 0, wx.ALL, 5 )
		
		
		bSizer61.Add( bSizer28, 0, 0, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.textKey = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_NOHIDESEL|wx.TE_READONLY|wx.TE_RICH|wx.TE_WORDWRAP|wx.VSCROLL )
		bSizer29.Add( self.textKey, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer29.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer61.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnEncode = wx.Button( self.panel1, wx.ID_ANY, u"Encode", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.btnEncode, 0, wx.ALL, 5 )
		
		self.textEncoded = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_NOHIDESEL|wx.TE_READONLY|wx.TE_RICH|wx.TE_WORDWRAP|wx.VSCROLL )
		bSizer71.Add( self.textEncoded, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer71.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer33.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnTakePhoto = wx.Button( self.panel1, wx.ID_ANY, u"Take Photo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnTakePhoto, 0, wx.ALL, 5 )
		
		self.imgQROutgoing = wx.StaticBitmap( self.panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		bSizer32.Add( self.imgQROutgoing, 0, wx.ALL, 5 )
		
		self.textImageWhatToDo = wx.StaticText( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textImageWhatToDo.Wrap( -1 )
		bSizer32.Add( self.textImageWhatToDo, 0, wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.panel1.SetSizer( bSizer33 )
		self.panel1.Layout()
		bSizer33.Fit( self.panel1 )
		bSizer5.Add( self.panel1, 1, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.m_menubar1.Append( self.menuFile, u"&File" ) 
		
		self.menuUsers = wx.Menu()
		self.menuItemManageUsers = wx.MenuItem( self.menuUsers, wx.ID_ANY, u"Manage Users", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuUsers.AppendItem( self.menuItemManageUsers )
		
		self.m_menubar1.Append( self.menuUsers, u"Users" ) 
		
		self.menuKeys = wx.Menu()
		self.menuItemCreateKeys = wx.MenuItem( self.menuKeys, wx.ID_ANY, u"Create Keys...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuKeys.AppendItem( self.menuItemCreateKeys )
		
		self.m_menubar1.Append( self.menuKeys, u"&Keys" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SET_FOCUS, self.OnSetFocus )
		self.cmbContactB.Bind( wx.EVT_COMBOBOX, self.eventCmbContactB )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnSave )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnOpen )
		self.textMessageText.Bind( wx.richtext.EVT_RICHTEXT_CHARACTER, self.EventOnRichTextCharacter )
		self.textMessageText.Bind( wx.richtext.EVT_RICHTEXT_CONTENT_INSERTED, self.EventOnRichTextCharacter )
		self.textMessageText.Bind( wx.richtext.EVT_RICHTEXT_DELETE, self.EventOnRichTextCharacter )
		self.textMessageText.Bind( wx.richtext.EVT_RICHTEXT_RETURN, self.EventOnRichTextCharacter )
		self.btnConvertToBinary.Bind( wx.EVT_BUTTON, self.OnShowAsBinary )
		self.btnLoadCurrentKey.Bind( wx.EVT_BUTTON, self.btnLoadCurrentKeyClick )
		self.btnEncode.Bind( wx.EVT_BUTTON, self.btnEncodeClick )
		self.textEncoded.Bind( wx.EVT_TEXT, self.textEncodedClick )
		self.btnTakePhoto.Bind( wx.EVT_BUTTON, self.btnTakePhotoClick )
		self.Bind( wx.EVT_MENU, self.OnManageUsersSelection, id = self.menuItemManageUsers.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCreateKeysMenu, id = self.menuItemCreateKeys.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSetFocus( self, event ):
		event.Skip()
	
	def eventCmbContactB( self, event ):
		event.Skip()
	
	def OnSave( self, event ):
		event.Skip()
	
	def OnOpen( self, event ):
		event.Skip()
	
	def EventOnRichTextCharacter( self, event ):
		event.Skip()
	
	
	
	
	def OnShowAsBinary( self, event ):
		event.Skip()
	
	def btnLoadCurrentKeyClick( self, event ):
		event.Skip()
	
	def btnEncodeClick( self, event ):
		event.Skip()
	
	def textEncodedClick( self, event ):
		event.Skip()
	
	def btnTakePhotoClick( self, event ):
		event.Skip()
	
	def OnManageUsersSelection( self, event ):
		event.Skip()
	
	def OnCreateKeysMenu( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgKeyManagement
###########################################################################

class dlgKeyManagement ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Manage Keys", pos = wx.DefaultPosition, size = wx.Size( 576,476 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Select both Contacts and create a keys for their relationship!", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE|wx.ALWAYS_SHOW_SB|wx.CLIP_CHILDREN )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer17.Add( self.m_staticText7, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFromMe = wx.StaticText( self, wx.ID_ANY, u"Contact A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFromMe.Wrap( -1 )
		bSizer12.Add( self.lblFromMe, 0, wx.ALL, 5 )
		
		self.txtContactA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.txtContactA, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer12, 1, 0, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFromOther = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFromOther.Wrap( -1 )
		bSizer13.Add( self.lblFromOther, 0, wx.ALL, 5 )
		
		cmbContactBChoices = []
		self.cmbContactB = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cmbContactBChoices, 0 )
		bSizer13.Add( self.cmbContactB, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer13, 1, 0, 5 )
		
		
		bSizer11.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Plug in two clean USB sticks and mount them", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE|wx.ALWAYS_SHOW_SB|wx.CLIP_CHILDREN )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetMinSize( wx.Size( -1,30 ) )
		
		bSizer20.Add( self.m_staticText71, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnMountUSBs = wx.Button( self, wx.ID_ANY, u"Mount both USB sticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.btnMountUSBs, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"are they both empty? Inform about existing content", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer20.Add( self.m_staticText13, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"create Keys, write on both USB sticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer21.Add( self.m_staticText14, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnCreateKeys = wx.Button( self, wx.ID_ANY, u"create Keys", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.btnCreateKeys, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnUnmountUSBs = wx.Button( self, wx.ID_ANY, u"Unmout both USB sticks", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.btnUnmountUSBs, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer191, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnMountUSBs.Bind( wx.EVT_BUTTON, self.btnMountUSBsClick )
		self.btnCreateKeys.Bind( wx.EVT_BUTTON, self.btnCreateKeysClick )
		self.btnUnmountUSBs.Bind( wx.EVT_BUTTON, self.btnUnmountUSBsClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnMountUSBsClick( self, event ):
		event.Skip()
	
	def btnCreateKeysClick( self, event ):
		event.Skip()
	
	def btnUnmountUSBsClick( self, event ):
		event.Skip()
	

###########################################################################
## Class dlgUserManagement
###########################################################################

class dlgUserManagement ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usermanagement", pos = wx.DefaultPosition, size = wx.Size( 463,499 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25.SetMinSize( wx.Size( -1,250 ) ) 
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"existing Users:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer25.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		listUsersChoices = []
		self.listUsers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), listUsersChoices, wx.LB_SINGLE )
		self.listUsers.SetMinSize( wx.Size( 200,120 ) )
		
		bSizer25.Add( self.listUsers, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"new Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer26.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txtNewUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.txtNewUsername, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddNewUser = wx.Button( self, wx.ID_ANY, u"Create New User", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnAddNewUser, 0, wx.ALL, 5 )
		
		self.btnDeleteUser = wx.Button( self, wx.ID_ANY, u"Delete User", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnDeleteUser, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtSelectedUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer23.Add( self.txtSelectedUser, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Is Active User?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer24.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.txtIsActiveUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer24.Add( self.txtIsActiveUser, 0, wx.ALL, 5 )
		
		self.btnMakeActiveUser = wx.Button( self, wx.ID_ANY, u"Make this user Active", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.btnMakeActiveUser, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.EventUsermanagementClose )
		self.listUsers.Bind( wx.EVT_LISTBOX, self.OnListUsersClick )
		self.btnAddNewUser.Bind( wx.EVT_BUTTON, self.btnAddNewUserClick )
		self.btnDeleteUser.Bind( wx.EVT_BUTTON, self.btnDeleteUserClick )
		self.btnMakeActiveUser.Bind( wx.EVT_BUTTON, self.btnMakeActiveUserClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def EventUsermanagementClose( self, event ):
		event.Skip()
	
	def OnListUsersClick( self, event ):
		event.Skip()
	
	def btnAddNewUserClick( self, event ):
		event.Skip()
	
	def btnDeleteUserClick( self, event ):
		event.Skip()
	
	def btnMakeActiveUserClick( self, event ):
		event.Skip()
	

