"""
eureka-Python Assignment
4. Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose if the entered string is: Python0325
Then the output will be:
LETTERS: 6
DIGITS:4
Hint: Use built-in functions of string.

about program : simple answer from the user and split the word in the sequence num caps small
"""
# numbers with list
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# alphabets with list three quotes to reduce length of lines
alphas = ''' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' '''

# get the sentence
string = input("Type or paste any sentences with numbers and letter: ")

# start from zero
calnums = 0
callets = 0

# iterate through all values
for s in string:
	if s in nums:
		calnums += 1
	# vlue increment
	elif s in alphas:
		callets += 1

print("Total letters in given sentence =", callets)
print("Total digits in given sentence =", calnums)
