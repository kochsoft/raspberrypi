#!/bin/python

"""
Script for direct control of argonone fan speed.

(Man, I hope, this won't break that thing.)

Markus-Hermann Koch / mhk@markuskoch.eu / 240414
"""

import sys
import os

sys.path.append("/etc/argon/")
from argonsysinfo import *
from argonregister import *


class FanControl:
	def __init__(self):
		# Initialize I2C Bus
		self.bus = argonregister_initializebusobj()
		self.argonregsupport = argonregister_checksupport(self.bus)

	"""
		:param speed: Value of fan speed in {0,..,100}.
	"""
	def set_fanspeed(self, speed: int):
		print(f"Attempting to set fan speed to {speed}%.")
		argonregister_setfanspeed(self.bus, speed, self.argonregsupport)

if __name__ == "__main__":
	val = None
	if 1 < len(sys.argv):
		try:
			val = int(sys.argv[1])
			if not (0 <= val <= 100):
				print("Error: Given value needs to be in {0,..,100}. " + f"However, {val} was given.")
				sys.exit(2)
		except Exception:
			print(f"Error: Cannot parse argument '{sys.argv[1]}' to int in " + "{0,..,100}.")
			sys.exit(1)
	else:
		print("Usage: $ ./fan_control.py val")
		print("  val in {0,..,100}. Will set the fan speed to the respective percentage.")
		sys.exit(0)
	controller = FanControl()
	controller.set_fanspeed(val)
	print("Done.")
