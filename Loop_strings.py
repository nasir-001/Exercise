# Authur: Nasir Lawal
# Date: 5th-Dec-2019

"""
Description: Take a user input string and display
string, one character at a time
"""

def main():

	# Using for loop
	user_input1 = input("Enter any string here\n")
	for a in user_input1:
		print(a)

	# Using whilr loop
	user_input2 = input("Enter any string here\n")
	while True:
		for a in user_input2:
			print(a)
		break

if __name__ == "__main__":
	main()