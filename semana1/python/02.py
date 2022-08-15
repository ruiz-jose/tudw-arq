# importing the module
import sys
	
# fetching the maximum value
max_val = sys.maxsize

try:

	# creating list with max size + 1
	list = range(max_val + 1)

	# displaying the length of the list
	print(len(list))
	print("List successfully created")
	
except Exception as e:

	# displaying the exception
	print(e)
	print("List creation unsuccessful")
