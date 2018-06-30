# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network

from machine import Pin

# Join a network

sta=network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("NETGEAR22","ancientstreet088")

# Create a network

ap=network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="\u219f\u219f\u219fWW\u219f\u219f\u219f", authmode=0)
ap.ifconfig(('10.0.0.1','255.255.255.0','10.0.0.1','10.0.0.1'))

# This is the signal to the AVR

p13 = Pin(13, Pin.OUT)
p13.value(1)

# RED Status LED shows if boot is ok (flashes during brownout)

p12 = Pin(12, Pin.OUT)
p12.value(1)