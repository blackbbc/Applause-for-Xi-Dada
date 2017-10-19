#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Connecting device..."
device = MonkeyRunner.waitForConnection()
print "Device connected!"

raw_input("Press Enter, then press Ctrl+D to start applausing...")

print "Start applausing..."

while (True):
    device.touch(500, 1600, MonkeyDevice.DOWN_AND_UP)
