# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.richtext
import os
import subprocess
import g

#file_usernames = 'D:/CPi/Uwe_Florian/users.txt'
file_usernames = '/home/pi/cpi/data/users.txt'

# this is how it is done in ./mounting.sh
path_usb_a = "/media/usb1/"
path_usb_b = "/media/usb2/"

###########################################################################
## Class GUI_MainFrame
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
		
		cmbContactAChoices = []
		self.cmbContactA = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cmbContactAChoices, 0 )
		bSizer12.Add( self.cmbContactA, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer12, 1, 0, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFromOther = wx.StaticText( self, wx.ID_ANY, u"Contact B", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		
		self.LoadUsers()
		self.Show()
		
	
	def btnMountUSBsClick( self, event ):
		subprocess.call("./mounting.sh")
	
	def btnCreateKeysClick( self, event ):
		event.Skip()
	
	def btnUnmountUSBsClick( self, event ):
		subprocess.call("./unmount.sh")
		
			
	def __del__( self ):
		pass
	
	def LoadUsers(self):
		lines = GetUsers()
		for i in lines:
			#print i, len(lines) #lines[i], len(w)
			s = i.split(';');
			#self.cmbMgmtKeysUser.Append(s[1]); #i
			self.cmbContactA.Append(s[1]);
			self.cmbContactB.Append(s[1]);
		#f.close()		

class GUI_MainFrame ( wx.Frame ):
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypto Pi", pos = wx.DefaultPosition, size = wx.Size( 910,630 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"&Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"&Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer6, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer4.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnConvertToBinary = wx.Button( self.m_panel1, wx.ID_ANY, u"Show as Binary", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.btnConvertToBinary, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL )
		bSizer51.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button41 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_button41, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL )
		bSizer61.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer61.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnEncode = wx.Button( self.m_panel1, wx.ID_ANY, u"Encode", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.btnEncode, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL )
		bSizer71.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer71.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer7 )
		self.m_panel1.Layout()
		bSizer7.Fit( self.m_panel1 )
		bSizer5.Add( self.m_panel1, 1, wx.EXPAND|wx.ALL, 5 )
		
		
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
		
		self.Show(True)
		
		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnSave )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnOpen )
		self.Bind( wx.EVT_MENU, self.OnManageUsersSelection, id = self.menuItemManageUsers.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCreateKeysMenu, id = self.menuItemCreateKeys.GetId() )
		
		
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class

	def OnManageUsersSelection(self, event):
		x=dlgUserManagement(None)

	def OnCreateKeysMenu( self, event ):
		#event.Skip()
		x = dlgKeyManagement(None)

	def OnExitClick( self, event ):
		event.Skip()
	
	def OnFileChanged( self, event ):		
		print self.m_filePicker2.ClassName
		print self.m_filePicker2.GetTextCtrlValue
	
	def OnOpen(self,e):
		#""" Open a file"""
		self.dirname= ''	        
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.m_richText1.SetValue(f.read())
			#f.close()
		dlg.Destroy()
	
	def OnSave( self, event ):
		# save file
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			t = self.m_richText1.GetValue()
			f = open(os.path.join(self.dirname, self.filename), 'w').write(t)
		dlg.Destroy()  #?

class dlgUserManagement ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usermanagement", pos = wx.DefaultPosition, size = wx.Size( 322,371 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"existing Users:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer15.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		listUsersChoices = []
		self.listUsers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listUsersChoices, wx.LB_SINGLE )
		self.listUsers.SetMaxSize( wx.Size( -1,50 ) )
		
		bSizer15.Add( self.listUsers, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"new Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer15.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.txtNewUsername = wx.TextCtrl( self, wx.ID_ANY, u"asd", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.txtNewUsername, 0, wx.ALL, 5 )
		
		self.btnAddNewUser = wx.Button( self, wx.ID_ANY, u"Create New User", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnAddNewUser, 0, wx.ALL, 5 )
		
		self.btnDeleteUser = wx.Button( self, wx.ID_ANY, u"Delete User", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnDeleteUser, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtSelectedUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer16.Add( self.txtSelectedUser, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.LoadUsers()
		
		self.Centre( wx.BOTH )
		self.Show()
		
		self.listUsers.Bind( wx.EVT_LISTBOX, self.OnListUsersClick )
		self.btnAddNewUser.Bind( wx.EVT_BUTTON, self.btnAddNewUserClick )
		self.btnDeleteUser.Bind( wx.EVT_BUTTON, self.btnDeleteUserClick )
	
	def LoadUsers(self):
		self.listUsers.Clear()
		lines = GetUsers()
		for i in lines:
			#print i, len(lines) #lines[i], len(w)
			s = i.split(';');
			self.listUsers.Append(s[1]); #i
		#f.close()		
	
	def OnListUsersClick( self, event ):
		lines = GetUsers()						
		i = self.listUsers.GetSelection()
		s = lines[i].split(';')
		self.txtSelectedUser.SetValue(s[1])
	
	def btnAddNewUserClick( self, event ):
		lines = tuple(open(file_usernames, 'r'))
		
		_maxIndex = 0
		for i in range(0,len(lines)):
			_currentIndex = int(lines[i].split(";")[0]) 
			if _currentIndex > _maxIndex:
				_maxIndex = _currentIndex		
		#print lines[0].split(";")[1]
		
		# get max index, +1 is the index for new User
		_newIndex = _maxIndex +1#getMaxIndex(file_usernames) + 1		
		_newUserName = self.txtNewUsername.GetValue()
		
		with open(file_usernames, "a") as _usernames:
			_usernames.write(str(_newIndex) + ";" + _newUserName + "\n")

		self.LoadUsers()
	
	def btnDeleteUserClick( self, event ):
		lines = GetUsers()
		j = self.listUsers.GetSelection()
		lines_new = ''
		for i in range(0, len(lines)):
			if i != j:
				lines_new += lines[i]
		
		#lines.remove(i)
		
		# update File
		with open(file_usernames, "w") as _usernames:  ## w -> overwrite, a -> append
			_usernames.write(lines_new)
		# refresh Listbox
		self.LoadUsers()
	
	def __del__( self ):
		pass
		


def GetUsers():
	lines = tuple(open(file_usernames, 'r'))
	return lines


	

# get rowcount of a file
def getMaxIndex(fname):
	_maxIndex = 0
	with open(fname) as f:
		for i, l in enumerate(f):
			_currentIndex = int(f[i].split(";")[0]) 
			if _currentIndex > _maxIndex:
				_maxIndex = _currentIndex
	return _maxIndex

	
app = wx.App(False)
frame = GUI_MainFrame(None)
app.MainLoop()

