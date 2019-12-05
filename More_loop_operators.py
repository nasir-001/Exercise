# Authur: Nasir Lawal
# Date: 5th-Dec-2019

"""
Description:  Create a fixed list or tuple of five
numbers and determine their average
"""

def main():

	tuple_item = (1, 2, 3, 4, 5)
	length = len(tuple_item)
	summation = sum(tuple_item)
	average = summation / length
	print(average)

if __name__ == "__main__":
	main()