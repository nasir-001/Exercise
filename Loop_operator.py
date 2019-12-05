# Authur: Nasir Lawal
# Date: 5th-Dec-2019

"""
Description: Create a fixed list or tuple of
five numbers and output their sum
"""

def main():

	# Summing the tuple 
	print("Using fixed value")
	tuples = (1, 2, 3, 4, 5)
	print(sum(tuples))

	# Having the user to enter the numbers and sum them
	print("\nCollecting the numbers from user")
	user_input = list(map(int, input()))
	print(sum(user_input))

	# Using while loop
	print("\n" + "Using while loop")
	user_input = list(map(int, input()))
	while True:
		count = 0
		num_list = []
		for x in user_input:
			num_list.append(x)
		print(sum(num_list))
		break

if __name__ == "__main__":
	main()