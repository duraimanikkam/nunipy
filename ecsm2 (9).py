"""
eureka-Python Assignment
5. Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.

"""


def isPalindrome(s):
#using reverse funtion
	rev = ''.join(reversed(s))

	# Checking if both string are
	# equal or not
	if s == rev:
		return True
	return False


# main function
s = input("type a word to check palindrome: ")
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")
