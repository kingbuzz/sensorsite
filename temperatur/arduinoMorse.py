#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Alejandro Gonzalez Barrera <alejandrok5@gmail.com>
# More info: http://alejandrok5.wordpress.com/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
from threading import Thread
import pyfirmata




PIN = 12 # Pin 12 is used
DELAY = 20 # A 2 seconds delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
PORT = 'COM5'

# Creates a new board
board = pyfirmata.Arduino(PORT)

# Loop for blinking the led

board.digital[PIN].write(1) # Set the LED pin to 1 (HIGH)
board.pass_time(DELAY)
board.digital[PIN].write(0) # Set the LED pin to 0 (LOW)
board.pass_time(DELAY)