#!/bin/sh

echo "unmount"
fuser -m /media/usb1
sudo umount -l /dev/sda1
sudo rm -r /media/usb1

fuser -m /media/usb2
sudo umount -l /dev/sdb1
sudo rm -r /media/usb2