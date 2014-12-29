from subprocess import call #, check_output
import os


import subprocess
print "start"

subprocess.call("./mounting.sh")


myfile = "/media/usb1/index.txt"

fh = open(myfile, 'w')
fh.write("id: 0001")
fh.write("date: 14.04.2014")
fh.write("Uwe's Keyfile with Florian")
fh.close()
fh = open(myfile, 'r')
print (fh.read())

myfile = "/media/usb2/index.txt"
fh = open(myfile, 'w')
fh.write("id: 0002")
fh.write("date: 14.04.2014")
fh.write("Florian's Keyfile with Uwe")
fh.close()
fh = open(myfile, 'r')
print (fh.read())


subprocess.call("./unmount.sh")
