"""

13.Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The
numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

"""
items = []
num = [x for x in input("accepts a sequence of comma separated 4 digit binary numbers: ").split(',')]
p = set(num)
s = {'0', '1'}
if s == p or p == {'0'} or p == {'1'}:
    for n in num:
        x = int(n, 2)
        if not x%5:
            items.append(n)
            print(','.join(items))
else :
        print("No")
