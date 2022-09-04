'''
3.A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

Hint: In case of input data being suppliedto the question, it should be assumed to be a console input.

'''
#add 0value to strings
l, u, s, d = 0, 0, 0, 0
str = input('Password:: ')
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
if (len(str)<=12 and len(str)>=8 ):
	for i in str:

		# counting lowercase alphabets
		if (i in smallalphabets):
			l+=1		

		# counting uppercase alphabets
		if (i in capitalalphabets):
			u+=1		

		# counting digits
		if (i in digits):
			d+=1		

		# counting the mentioned special characters
		if(i in specialchar):
			s+=1	
if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(str)):
	print("Valid Password")
else:
	print("Invalid Password")
