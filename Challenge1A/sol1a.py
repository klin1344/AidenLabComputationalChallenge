"""
Aiden Lab Computational Challenge 1A
Author: Kevin Lin 
"""
import sys
import itertools
import math

def can_reach_value(lower_bound, upper_bound, target, buckets):
	"""
	Given a lower bound, upper bound, target value, and list of buckets, generates 
	Cartesian products of from length lower_bound to upper_bound with the list of buckets 
	and returns True if the sum is equal to the target, False otherwise.
	"""

	# generate all Cartesian products with lengths from lower_bound to upper_bound
	for idx in range(lower_bound, upper_bound + 1):
		for prod in itertools.product(buckets, repeat=idx):
			# if the sum is the target value, we have successfully reached the target
			sum_buckets = sum(prod)
			if sum_buckets == target:
				return True
	return False

if len(sys.argv) != 3:
	print "ERROR: You must run the program with two arguments: <target> <buckets>"

else:
	# parse and store the <target> and <buckets> arguments
	target = int(sys.argv[1])
	buckets = [int(char) for char in list(sys.argv[2].replace("[", "").replace("]", "").split(","))]

	# if target is divisible by any bucket, then we can reach the target
	if True in [target % bucket == 0 for bucket in buckets]:
		print True
		exit()
	# otherwise, we have to use the Cartesian product
	else:
		# find the smallest and largest lengths that the Cartesian product can be
		lower_bound = target // max(buckets)
		# upper_bound is rounded up to ensure we generate a large enough Cartesian product
		upper_bound = int(math.ceil(float(target) / min(buckets)))

		print can_reach_value(lower_bound, upper_bound, target, buckets)