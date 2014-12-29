#!/bin/sh
echo "Installation Instructions for CPi"
# based on a plain Raspbian image summer 2014

# execute with chmod -x install1.sh
# sudo rpi-update

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get install python-imaging
sudo apt-get install python-imaging-tk

sudo apt-get -y install python-qrtools
sudo apt-get -y install qtqr

sudo apt-get -y install python-picamera
sudo apt-get -y install python-imaging-tk

# for gui

sudo apt-get -y install python-wxgtk2.8  
sudo apt-get -y install python-wxtools
sudo apt-get -y install wx2.8-i18n
sudo apt-get -y install libwxgtk2.8-dev
sudo apt-get -y install libgtk2.0-dev

# testing random quality

sudo apt-get -y install ent
sudo apt-get -y install dieharder

sudo mkdir /home/pi/cpi
sudo mkdir /home/pi/cpi/gpio
sudo mkdir /home/pi/cpi/gpio/bigrandomfiles