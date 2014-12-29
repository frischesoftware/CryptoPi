# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import os
from datetime import datetime
import shutil
from Classes import *

class g():
        #def start(self, _contactA, _contactB):
        def start(self, CONTACT_A, CONTACT_B):                
                print CONTACT_A
                print CONTACT_B
                # read from GPIO pin #2, BCM-mode
                pin = 2
                GPIO.setmode(GPIO.BCM)                
                GPIO.setup(pin, GPIO.IN)
                 
                # 160 character/ message -> 1280 bits. 100 files each ->> 256000 bits
                total_length = 512000 #128000
                number_of_files = 100
                length_of_file = total_length / number_of_files
              
                #  - From Hardware RNG: true randomness and trust
                ###_trng= "".join([str(GPIO.input(pin)) for num in xrange(total_length)])
                ###self.writeFile(TRNG, _trng)
                _trng = open(BASIC_PATH+TRNG, 'r').read()
                

                #  - From Linux RNG: entropy and reliability
                _prng= "".join([str(bin(ord(os.urandom(1)))[2:]).zfill(8) for num in xrange(total_length/8)])
                self.writeFile(PRNG, _prng)                                


                #  - XOR
                p = _trng
                k = _prng
                c = ''
                
##                _counter = 0
##                for char in _trng:
##                    _counter +=1
##                    try:        
##                        c = c + str(int(char, 2) ^ int(k[0],2))
##                        k = k[1:] #removes first char
##                    except IndexError:
##                        print "Index Error, gecatcht!"
##                        print "_counter: " + str(_counter)
##                        print str(len(_trng)) + " - " + str(len(_prng))
##                        
##                self.writeFile(BIG_RNG, c)
                


                # 3. split the big file in small ones

                # 3a. split big file in half (one for sending, one for receiving)

                f = open(BASIC_PATH + BIG_RNG, 'r')
                #text = f.read()
                text=_prng
                print str(len(_prng))

                text_a, text_b = text[:len(text)/2], text[len(text)/2:]

                # build the path
                
                
                # delete all previously existing keyfiles. Start fresh...

                self.deleteKeyFiles(KEY_DIR_A, CONTACT_A, CONTACT_B)
                self.deleteKeyFiles(KEY_DIR_B, CONTACT_A, CONTACT_B)

                # write the files                        
                self.writeFiles(number_of_files, KEY_DIR_A, text, 0, CONTACT_A, CONTACT_B)            
                self.writeFiles(number_of_files, KEY_DIR_B, text, 256000, CONTACT_B, CONTACT_A)

        def writeFile(self, _filename, _content):
                f = open(BASIC_PATH + _filename, 'w')                
                f.write(_content)
                f.close()
        

        def deleteKeyFiles(self, _keydir, sender, receipient):
                print "deleteKeyFiles"
                _path =  _keydir + sender + "/" + receipient # + "/"
                print _path
                #for _currentfile in os.listdir(_path):                
                #fpath = os.path.join(_path, _currentfile)
                if os.path.exists(_path):
                        try:
                                if os.path.isfile(fpath):
                                        os.unlink(fpath)
                        except Exception, e:
                                print e
                print "*********************"
                
      
        def writeFiles(self, _number_of_files, _keydir, _text, _startindex, sender, receipient):
        #def writeFiles(self, _number_of_files, _path, _text, _startindex):                
                for i in range(0, _number_of_files):
                        print "writeFiles" + str(i) + " - " + str(len(_text))
                        _from = i*2560 + int(_startindex)
                        _to = (i+1)*2560 + int(_startindex)

                        _path = GetPathToKeyfile(_keydir, sender, receipient)         
                        #g = open(_keydir + str(i), 'w') ##ohne KEY_BASE_NAME +
                        
                        print "_path: " + _path
                        if not os.path.exists(_path):
                                os.makedirs(_path)                                
                        g = open(_path + str(i), 'w') #mit Pfaden
                        g.write(str(sender) + "; " + " to" + str(receipient) + ";")
                        #g.write("from : " + str(sender) + "\n")
                        #g.write("to : " + str(receipient) + "\n")
                        g.write(_text[int(_from): int(_to)])
                        g.close
                        

#__x = str(datetime.now().strftime('%Y-%m-%d %H:%m:%S||'))
