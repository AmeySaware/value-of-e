# Created by Amey Saware
# Version 0.0

"""
In the book "The Simpsons and their mathematical secrets" Simon Singh states that if you generate random numbers and add them, the average of numbers required for the sum to exceed 1 tends to e as number of trials tends to infinity.
This program tests this conjucture for its validity by monte carlo trails and checking accuracy against standard value of e.
""" 

import random

def mctrial():

	"""
	Runs one instance of monte carlo trial and returns the result
	"""

	total = 0
	count = 0
	
	while total <= 1:
		new_num = random.random()
		count += 1
		total += new_num
		pass
	return count

def mctest(num_trials):

	"""
	Runs the specified number of trials and prints the output of the average result
	"""

	result = []

	for trial in range(num_trials):
		result.append(mctrial())

#	print result
#	print sum(result)
	print float(sum(result))/num_trials

	pass

mctest(int(10E6))