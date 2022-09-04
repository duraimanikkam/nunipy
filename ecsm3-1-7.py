"""
7. Write a program which can compute the factorial of a given numbers. Use recursion
to find it. 
Hint: Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""


def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)

# execution
enn = int(input("input whole numbers: "));
print("Factorial of", enn, "is",
factorial(enn),"using recursive")
