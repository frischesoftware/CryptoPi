# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
#import time

#import random
#from random import *
#from os import urandom
import os
#import re
from datetime import datetime


GPIO.setmode(GPIO.BCM)


#f = open('trnd.txt', 'w')

# GPIO = the pins where the hardware RNG is plugged in. Configure to read from pin #2
pin = 2
GPIO.setup(pin, GPIO.IN)

# number of files, and how much random bits in each file to match message length?
# (message length depends on QR code capacity)
# 160 characters == 1280 bits, 100 files, in two sets (one to send, one to receive)
 

total_length = 256000 #128000
number_of_files = 100
length_of_file = total_length / number_of_files

name_a = "Alice"  # this Alice's File which she will use to send msg. to Bob
name_b = "Bob" # Bob will encrypt with this, and send to Alice

# some file paths
basic_path = "/home/pi/cpi/gpio/"
big_true_rng = "bigrandomfiles/trng.txt"
big_prng = "/home/pi/cpi/gpio/bigrandomfiles/prng.txt"
big_rng = "/home/pi/cpi/gpio/bigrandomfiles/rng.txt"
individual_rnd_files_a = "smallrandomfiles_a/rnd"
individual_rnd_files_b = "smallrandomfiles_b/rnd"

# 1. make big files, so that randomness can be tested on the full data

#  - From Hardware RNG:
f = open(basic_path + big_true_rng, 'w')
f.write("".join([str(GPIO.input(pin)) for num in xrange(total_length)]))
f.close()

#  - From Pseudo RNG:
g = open(basic_path + big_prng, 'w')
g.write(os.urandom(total_length/8))
g.close

# 2. XOR both RNGs to combine both advantages:
#       - true randomness, trust from TRNG
#       - good random properties, reliability from PRNG

_trng_txt = open(basic_path + big_true_rng, 'r').read()

_prng_txt_temp = open(big_prng, 'r').read()

_prng_txt = ''
for char in _prng_txt_temp:
        _prng_txt = _prng_txt + (str(bin(ord(char))[2:])).zfill(8)

#vgl Editor3
p = _trng_txt
k = _prng_txt
c = ''

# XOR PRNG and TRNG ...
#_counter = 0
#for char in _trng_txt:
    #_counter +=1
    #try:        
        #c = c + str(int(char, 2) ^ int(k[0],2))
        #k = k[1:] #removes first char
    #except IndexError:
        #print "Index Error, gecatcht!"
        #print "_counter: " + _counter
        #print str(len(_trng_txt)) + " - " + str(len(_prng_txt))
        
# ... and save results in file

#x = open(big_rng, 'w')
#x.write(c)
#x.close()



# 3. split the big file in small ones

# 3a. split big file in half (one for sending, one for receiving)

f = open(big_rng, 'r')
text = f.read()

text_a, text_b = text[:len(text)/2], text[len(text)/2:]

print "textlaenge: " + str(len(text))
print "text_a: " + str(len(text_a))
print "text_b: " + str(len(text_b))



for i in range(0 , number_of_files):  #128000/1280 = 100
        g = open(individual_rnd_files_a + str(i), 'w')

        #%Y-%m-%d
        print "Alice ; Alice to Bob; " + datetime.now().strftime('%Y-%m-%d %H:%m:%s')
        g.write("Alice ; Alice to Bob; " + datetime.now().strftime('min: %m ; %Y-%m-%d %H:%m:%S||'))
        
        _from = i*1280
        _to = (i+1)*1280
        
        g.write(text[_from:_to])
        g.close



for i in range(0 , number_of_files):  #128000/1280 = 100
        g = open(individual_rnd_files_b + str(i), 'w')        
        g.write("Bob ; Bob to Alice; " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        _from = i*1280
        _to = (i+1)*1280
        
        g.write(text[_from:_to])
        g.close









#for file_nr in range(1,number_of_files):
#        f = open('trng' + str(file_nr) , 'w')        
#        f.write("".join([str(GPIO.input(pin)) for num in xrange(1024)]))
#        f.close()        

#g = open('prng.txt', 'w')
#for i in range (0,10):
        #print getrandbits(1) #choice([0, 1])
#        y = str(getrandbits(1))
#        g.write(x)
#        time.sleep(0.1)
#g.close()
