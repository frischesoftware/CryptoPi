# -*- coding: utf-8 -*-
import wx
import wx.richtext
import os

import re

from gui import dlgKeyManagement
from gui import GUI_MainFrame
from gui import dlgUserManagement
from DerivedDlgUserManagement import DerivedDlgUserManagement
from DerivedDlgKeyManagement import DerivedDlgKeyManagement

from Classes import *

from qrtools import QR
import sys
import glob

#for taking photos:
import picamera
import time
##import PIL
##from PIL import image



class MyApplication(GUI_MainFrame):
    def __init__(self, *args, **kargs):
        GUI_MainFrame.__init__(self, *args, **kargs)
        self.LoadUsers()
        #self.LoadCurrentKeyfileForSelectedContacts()

    def EventOnRichTextCharacter( self, event ):
        print "hi"
	self.lblTextLength.SetLabel(str(len(self.textMessageText.GetValue())))
		
    def btnTakePhotoClick(self, event):
        qr = QR()
        i = 0
        while qr.data == "NULL":
        #while i == 0:
            _filename = '/home/pi/cpi/camera' + str(i) + '.jpg'
            camera = picamera.PiCamera()
            camera.resolution = (300, 300)
            camera.capture(_filename)
            print "gecaptured: " + _filename
            z = qr.decode(_filename)
            print z


            
            bm = wx.Image(_filename, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            
            #bitmap = wx.Bitmap(QR_IMAGE_FILE)
            #bitmap = self.scale_bitmap(bitmap, 300, 300)    
            #control = wx.StaticBitmap(self, -1, bitmap)
            #control.SetPosition((10, 10))
		
            self.imgQROutgoing.SetBitmap(bm)
            self.textImageWhatToDo.Label="Message: " + qr.data
            #self.Refresh()
            self.Update()
            print "refreshed" 
            #im = Image.open('/home/pi/cpi/camera' + str(i) + '.jpg')
            #pho = ImageTk.PhotoImage(im)
            #label = Label(image = pho)
            #label.image = pho
            #label.pack()
            ##root.update()
            ###frame.update()
            #self.ph.image = pho
            
            
            print "bild camera" + str(i) + ".jpg angezeigt"
            time.sleep(1)
            camera.close()
                #qr.destroy()
            i = i + 1
            print "i ist jetzt: " + str(i)
            print "--------------------------------------"
	
    def OnManageUsersSelection( self, event ):
        #event.Skip()
       #x = dlgUserManagement(None)
        x = DerivedDlgUserManagement(None)
        x.Show()
        x.LoadUsers()  # "From" and "To"

    def eventCmbContactB(self, event):
        print str(self.cmbContactB.GetStringSelection())
        self.LoadCurrentKeyfileForSelectedContacts()


    def ResetAllTextboxes(self):
        self.textMessageText.SetValue("")
        self.textBinaryText.SetValue("")
        self.textKey.SetValue("")
        self.textEncoded.SetValue("")
        self.lblTextLength.SetLabel("0")
    
    def LoadCurrentKeyfileForSelectedContacts(self):
	# Durchsuche den Ordner KEY_DIR_A nach rndX - Dateien und nehme die naechste

        #print "dropdown - text: " + str(self.cmbContactB.GetStringSelection())
        _path = GetPathToKeyfile(KEY_DIR_A, self.txtContactA.GetValue(), str(self.cmbContactB.GetStringSelection()))
        
	#print "PATH: " + _path
        if os.path.exists(_path):
            self.ResetAllTextboxes()
            self.textMessageText.SetEditable(True)
            
            myfiles = os.listdir(_path)
            print myfiles
            smallest = 999
            for i in range(0, len(myfiles)):	
                #if re.match('^rnd', str(myfiles[i])):
                #if myfiles[i].startswith("rng"):
                #myfiles[i] = myfiles[i].partition('rng')[2]
                if int(myfiles[i]) < int(smallest):
                    print "myfiles: " + myfiles[i] + " - smallest : " + str(smallest)
                    smallest = myfiles[i]
                        
            #print myfiles
            self.textCurrentKey.SetValue(str(smallest)) #"rnd" +
	else:
            self.ResetAllTextboxes()         
            self.textMessageText.SetValue("please generate Keys first")
            self.textMessageText.SetEditable(False)
        
    def btnLoadCurrentKeyClick(self, event) :
        _path = GetPathToKeyfile(KEY_DIR_A, self.txtContactA.GetValue(), str(self.cmbContactB.GetStringSelection()))
        self.textKey.Clear()
        #s = LoadKeyfile(KEY_DIR_A + "\\" + self.textCurrentKey.GetValue())
        print _path + self.textCurrentKey.GetValue()  #KEY_DIR_A
        s = LoadKeyfile(_path + self.textCurrentKey.GetValue()) #KEY_DIR_A
        self.textKey.SetValue(s[2])
        # determine and set max. message length based on key length:
        self.textMaxMessageLength.SetValue(str(len(s[1])/8))

	# ENCODE
    def btnEncodeClick( self, event ):
	
	p = self.textBinaryText.GetValue()
	k = self.textKey.GetValue()     
	c = ''
	for z in range(0, len(p)):
	    c = c + str(int(p[z],2) ^ int(k[z],2))

	self.textEncoded.Clear()
	self.textEncoded.SetValue(c)
	
	#Save File - braucht man?
	open(PLAINTEXT_FILE, 'w').write(c)
	
	#make QR
	self.makeQR(c)
	
	#show QR on screen
	# dies ist fuer Windows
	bitmap = wx.Bitmap(QR_IMAGE_FILE)
	bitmap = self.scale_bitmap(bitmap, 300, 300)    
	#control = wx.StaticBitmap(self, -1, bitmap)
	#control.SetPosition((10, 10))
		
	self.imgQROutgoing.SetBitmap(bitmap)
	self.textImageWhatToDo.Label="This is your message. Take a photo with your phone or webcam and send to recepient"
	
	
    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
	image = image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)
        result = wx.BitmapFromImage(image)	
	return result




    def makeQR(self, _data ):
	myCode = QR(data=_data, pixel_size=12, level='L')
	myCode.encode(QR_IMAGE_FILE)
	
	###conv = glob.glob('D:/CPi/data/encoded.png')
	###for cc in conv:
	    ###im = PIL.Image.open(cc)
	    ###im.save('D:/CPi/data/encoded.png', 'GIF')
    

    def EventUsermanagementClose( self, event ):
	self.LoadUsers()
	print "should change??"

    def OnSetFocus( self, event ):
	self.LoadUsers()
	print "focus erhalten, alles geupdated?"
	self.color = '#0099f7'
        self.Refresh()

    # wo ist der Update-Button?
    def btnUpdateClick( self, event ):
	self.LoadUsers()

    def OnCreateKeysMenu( self, event ):
        x = DerivedDlgKeyManagement(None)	
        x.Show()
	x.LoadUsers()
    
    def LoadUsers(self):
	self.cmbContactB.Clear()
	lines = GetUsers()
	for i in lines:
		#print i, len(lines) #lines[i], len(w)
		s = i.split(';');
		#self.cmbMgmtKeysUser.Append(s[1]); #i
		#self.cmbContactA.Append(s[1]); #this is now a textbox with the "Active" user, see below this
		if s[2].startswith('true'):
		    self.txtContactA.SetValue(s[1])
		else:	    		    
		    self.cmbContactB.Append(s[1])	
    
    def getTheActiveUser(self):
    	with open(file_usernames, 'r') as file:
	    data = file.readlines()
	
	for i in range(0, len(data)):
	    line = data[i]
	    if ";" in line:
		s = line.split(';')
		print s
		if s[2].startswith('true'):
		    print s[2]
		    return str(s[1])
		    #line = str(s[0] + ";" + s[1]+ ";" + s[2]) # reassemble the line
		    #data[i] = line
		else:
		    return "[no Active User]"
	
    
    def OnShowAsBinary(self, event):
	self.textBinaryText.Clear #delete("1.0", "end")
	plaintext = self.textMessageText.GetValue() #("1.0", END + '-1c')
	s = ''
	for char in plaintext:
	    s = s + (str(bin(ord(char))[2:])).zfill(8)
	    self.textBinaryText.SetValue(s)

    def OnBbtnLoadSelectedKey(self):
	f = open()
    


    
    def OnExitClick(self,event):
        event.Skip()


    def OnFileChanged( self, event ):
            print self.m_filePicker2.ClassName
            print self.m_filePicker2.GetTextCtrlValue
    
    def OnOpen(self,e):
        #""" Open a file"""
        self.dirname= ''     
        dlg = wx.FileDialog(self, "Choose a file", PLAINTEXT_PATH, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.textMessageText.SetValue(f.read())
                #f.close()
        dlg.Destroy()

    def OnSave( self, event ):
        # save file
        dlg = wx.FileDialog(self, "Save file as...", PLAINTEXT_PATH,
                            "draft.txt", "*.*", style = wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            f = open(path, 'w')
            f.write(self.textMessageText.GetValue())
            f.close()
        dlg.Destroy()


if __name__ == '__main__':

    app = wx.App(False)
    frame = MyApplication(None)
    frame.Show()
    app.MainLoop()      

#app = wx.App(False)
#frame = GUI_MainFrame(None)
#app.MainLoop()
