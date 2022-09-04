"""
5. Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input, the software should
provide required output.
Hint: Use if else statements and functions

"""

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
	def __init__(self):
		self.pwd = 12345
		self.balance=1000
		print("Hello!!! Welcome to Edu Bank")

	def Credit(self):
		amount=float(input("Enter amount to be Cash Credited: "))
		self.balance += amount
		print("\n Cash Amount Credited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

	def password(self):
		pwd = int(input("Enter password: "))
		if self.pwd == pwd:
			print("\n Login Successful")
		else:
			print("\n Wrong Password ")
			exit()
	def cpassword(self):
		pwd = int(input("Enter current password: "))
		while self.pwd == pwd:
			pwda = int(input("Enter New password: "))
			pwdb = int(input("Enter New password Again: "))
			if pwdb != pwda:
				print("\n Password not matched try again")
				return()
			else:
				self.pwd = pwdb
				print("\n Password Change Successful")
				s.display()
				exit()
		if self.pwd != pwd:
			print("\n You are not authorised to use this account")
			exit()

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.password()
s.display()
s.withdraw()
s.Credit()
s.display()
s.cpassword()
