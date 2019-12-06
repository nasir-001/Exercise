# Authur: Nasir Lawal
# Date: 5th-Dec-2019

"""
Descirption: Write a program to have the user input three (3)
numbers
"""

def main():

	print("Enter a number\nFormat:Initial Ending inrement:")
	user_input = list(map(str, input().strip().split()))
	init, end, step = int(user_input[0]), int(user_input[1]), int(user_input[2])

	for x in range(init, end, step):
		print(x)
	print(end)

if __name__ == "__main__":
	main()