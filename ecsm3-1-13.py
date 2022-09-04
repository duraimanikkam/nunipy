"""

13.Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The
numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

"""
while True:
    try:
        items = []
        num = [x for x in input("accepts a sequence of comma separated 4 digit binary numbers: ").split(',')]
        for p in num:
            x = int(p, 2)
            if not x%5:
                items.append(p)
        print(','.join(items))
        
        break
# except make output for other inputs with error information and continue until getting the integer
    except ValueError:
        print("please input comma separated 4 digit binary numbers")
        continue