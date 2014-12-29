from gui import dlgKeyManagement
from gui import GUI_MainFrame
from gui import dlgUserManagement
from g import g

import subprocess

from Classes import *

class DerivedDlgKeyManagement(dlgKeyManagement):
    def LoadUsers(self):
	self.cmbContactB.Clear()
	lines = GetUsers()
	for i in lines:
	    s = i.split(';');
	    if s[2].startswith('true'):
		self.txtContactA.SetValue(s[1])
	    else:	    		    
	        self.cmbContactB.Append(s[1])	
    
    def btnMountUSBsClick( self, event ):
	    subprocess.call("./mounting.sh")
    
    # create the Random Files (both)	
    def btnCreateKeysClick( self, event ):
	    #subprocess.call("./g.py")
            _g = g()
            print "g: CONTACT_A: " + self.txtContactA.GetValue()
            print "g: CONTACT_B: " + str(self.cmbContactB.GetStringSelection())
            CONTACT_A = self.txtContactA.GetValue()
            CONTACT_B = str(self.cmbContactB.GetStringSelection())
            #_g.start(self.txtContactA.GetValue(), str(self.cmbContactB.GetStringSelection()))
            _g.start(CONTACT_A, CONTACT_B)
    
    # unmount the USB sticks
    def btnUnmountUSBsClick( self, event ):
	    subprocess.call("./unmount.sh")
