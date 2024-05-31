from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/tty.usbserial-110", 9600)
device.open() 
device.send_data_broadcast("Hello XBee World!")
device.close()

