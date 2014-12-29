from gui import dlgKeyManagement
from gui import GUI_MainFrame
from gui import dlgUserManagement

from gui import GUI_MainFrame

from Classes import *

_selectedUserID = 0

class DerivedDlgUserManagement(dlgUserManagement):

    def EventUsermanagementClose(self, event):
        print "closed!!!11"
        self.Destroy()

    def LoadUsers(self):
        self.listUsers.Clear()
        with open(file_usernames, 'r') as file:
	    data = file.readlines()
	    for i in range(0, len(data)):
		line = data[i]
		if ";" in line:
		    s = line.split(';');
		    self.listUsers.Append(s[1])
	    
	    
    def btnMakeActiveUserClick(self, event):
	global _selectedUserID
	__selectedUserID = _selectedUserID
	
	self.LoadUsers() #refresh
	
	#read file
	with open(file_usernames, 'r') as file:
	    data = file.readlines()

	# make all users "false" (not active)
	for i in range(0, len(data)):
	    line = data[i]
	    if ";" in line:
		s = line.split(';')		
		s[2] = "false"
		line = str(s[0] + ";" + s[1]+ ";" + s[2]) # reassemble the line
		data[i] = line	
	
	print "!!!__selectedUserID:" + str(__selectedUserID) #"self.listUsers.GetSelection()" #+ str(self.listUsers.GetSelection()	
	
	line = data[int(__selectedUserID)]  # get the line that corresponds to the selected user		
	if ";" in line:
	    s = line.split(';')
	    s[2] = "true"  # set 3rd entry to "true"
	    line = str(s[0] + ";" + s[1]+ ";" + s[2]) # reassemble the line
	    data[int(__selectedUserID)] = line
		
    
	with open(file_usernames, 'w') as file:
	    for i in range(0, len(data)):
		if ";" in data[i]:		    
		    file.writelines(data[i] + "\n")
	
	# releselect the user again
	self.listUsers.SetSelection(int(__selectedUserID))

	# refresh the textboxes based on selection
	i = self.listUsers.GetSelection()
	s = data[i].split(';')
	print "hat der hier ein unicode symbol? " + s[2]
    	self.txtIsActiveUser.SetValue(s[2])


    def writeToFile(self, _lines):
	print "write to file"
	with open(file_usernames, "w") as _usernames:
	    for i in range(0, len(_lines)):		
		_usernames.write(_lines[i])

    def getSelectedUserID(self):
	i = self.listUsers.GetSelection()

    def OnListUsersClick( self, event ):
	lines = GetUsers()
	i = self.listUsers.GetSelection()
	s = lines[i].split(';')
	global _selectedUserID 
	_selectedUserID = s[0]	
	self.txtSelectedUser.SetValue(s[1])
	print "was ist mit s[2]? --" + s[2].rstrip() + "--"
	self.txtIsActiveUser.SetValue(s[2].rstrip())
	#print "self.listUsers.GetSelection()" + str(self.listUsers.GetSelection())
	_selectedUserID = str(self.listUsers.GetSelection())
	print "OnListUsersClick  _setselection =" + str(_selectedUserID)

    def btnAddNewUserClick( self, event ):
	lines = tuple(open(file_usernames, 'r'))
	#print "-------------"
	_maxIndex = 0

	#determine maxIndex:
	if len(lines) == 0:
	    _newIndex = 1
	else:
	    for i in range(0, len(lines)):
		_currentIndex = int(lines[i].split(";")[0])
		if _currentIndex >= _maxIndex:
		    _maxIndex = _currentIndex
		    #print _maxIndex #lines[0].split(";")[1]
	    _newIndex = _maxIndex +1

	_newUserName = self.txtNewUsername.GetValue()
	_isActive = "false";  # new users are not active users
	print "new line would be: " + str(_newIndex) + ";" + _newUserName + "\n"
	with open(file_usernames, "a") as _usernames:
		_usernames.write(str(_newIndex) + ";" + _newUserName + ";" + _isActive + "\n")

	self.LoadUsers()

		
	
    def btnDeleteUserClick( self, event ):
	    lines = GetUsers()
	    j = self.listUsers.GetSelection()
	    lines_new = ''
	    for i in range(0, len(lines)):
		    if i != j:
			    lines_new += lines[i]
	    # update File
	    with open(file_usernames, "w") as _usernames:  ## w -> overwrite, a -> append
		    _usernames.write(lines_new)
	    # refresh Listbox
	    self.LoadUsers()

    def __del__( self ):
	    pass

