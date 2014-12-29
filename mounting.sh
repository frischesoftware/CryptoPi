#!/bin/sh
# chmod a+x ./mounting.sh
echo "mount the USB"

echo "fertig"

sudo mkdir /media/usb1
sudo chmod -R 0777 /media/usb1
sudo mount -t vfat /dev/sda1 /media/usb1 -o rw


sudo mkdir /media/usb2
sudo chmod -R 0777 /media/usb2
sudo mount -t vfat /dev/sdb1 /media/usb2 -o rw




# wie unmounten?
### fuser -m /media/usb
# sudo umount -l /dev/sda1