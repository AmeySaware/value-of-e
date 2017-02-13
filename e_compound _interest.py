#Created by Amey Saware

"""
Euler's constant represents natural growth over time. So value of unit capital with infinitismal interst rate and infinite time should be e.
This program can be uses this fact to generate values of e. 
"""

def comp_int(period):

	rate = float(1)/period

	print (1+rate)**period

	pass

comp_int(10000000000000)