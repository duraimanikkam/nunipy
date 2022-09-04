"""

14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters.Suppose the following input is supplied to the program:Hello world!Then, the output should be:UPPER CASE 1LOWER CASE 9

"""
str = input('How are you?: ')

uc = sum(i.isupper() for i in str)
lc = sum(i.islower() for i in str)

print("UPPER CASE",uc,"LOWER CASE",lc)