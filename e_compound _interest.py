#Created by Amey Saware

"""
Euler's constant represents natural growth over time. So value of unit capital with infinitismal interst rate and infinite time should be e.
This program can be uses this fact to generate values of e. 
"""

def comp_int(period):

	rate = float(1)/period
	value = 1

	for tick in range(period):
		value *= (1 + rate)
		pass

	print value
		
	pass

comp_int(100000000)