# -*- coding: utf-8 -*-
file_usernames = 'users.txt'

# this is how it is done in ./mounting.sh

# use KEY_DIR_A...
#path_usb_a = "/media/usb1/"
#path_usb_b = "/media/usb2/"



BASIC_PATH = "/home/pi/cpi/gpio/bigrandomfiles/"
TRNG = 'trng.txt'
PRNG = 'prng.txt'
BIG_RNG = "rng.txt"

KEY_DIR_A = '/media/usb1/'
#KEY_DIR_A = 'D:/CPi/data/A/'

KEY_DIR_B = '/media/usb2/'
#KEY_DIR_B = 'D:/CPi/data/B/'
KEY_BASE_NAME = 'rnd'  # rnd komplett weglassen

CONTACT_A = ''
CONTACT_B = ''

#PLAINTEXT_FILE = 'D:/CPi/data/cryptotext.txt'
PLAINTEXT_FILE = '/home/pi/cpi/gpio/cryptotext.txt'

#QR_IMAGE_FILE = 'D:/CPi/data/text-plain.png'
QR_IMAGE_FILE = '/home/pi/cpi/gpio/qr.png'

#Drafts (Plaintext)
PLAINTEXT_PATH = '/home/pi/cpi/'

def GetUsers():
    lines = tuple(open(file_usernames, 'r'))
    #return nonempty lines
    _lines = []
    for l in lines:
	if len(l) >0:
	    _lines.append(l)    
   # print "Classes: " + str(_lines)
    return _lines

def LoadKeyfile(_filename):
    lines = tuple(open(_filename, 'r'))
    _lines = []
    for l in lines:
	if len(l) >0:
	    _lines.append(l)
    return _lines
	    

def GetPathToKeyfile(_keydir, sender, receipient):
    print "_keydir: " + _keydir
    print "sender: " + sender
    print "rec: " + receipient
    return _keydir + sender + "/" + receipient + "/"
    


# get rowcount of a file
def getMaxIndex(fname):
	_maxIndex = 0
	with open(fname) as f:
		for i, l in enumerate(f):
			_currentIndex = int(f[i].split(";")[0]) 
			if _currentIndex > _maxIndex:
				_maxIndex = _currentIndex
	return _maxIndex



		    
		    
		    
