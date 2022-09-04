'''
You have to use fundamentals of Python taught in module 2
1.Read the input from command line –Reference ID
2.Check for validity –
it should be 12 digits and allows on number and alphabet

For windows 
try 
py -m pip install maskpass
py -m pip install rsa

For linux
try 
pip install maskpass
pip install rsa

then run this code

'''
import maskpass
import rsa

#add 0value to strings

publicKey, privateKey = rsa.newkeys(512)
l, d = 0, 0
str = maskpass.askpass('Reference ID: ')
lc="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
if (len(str)==12 ):
	for i in str:

		# counting lowercase alphabets
		if (i in lc):
			l+=1	

		# counting digits
		if (i in digits):
			d+=1
    
if (l>=1 and d>=1 and l+d==len(str)):
    eid = rsa.encrypt(str.encode(),
                            publicKey)
    print("Valid Reference ID")
    print("Encoded RID",eid)
else:
	print("Invalid Reference ID")
    
    
