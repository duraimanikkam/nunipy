"""
eureka-Python Assignment
1. Write a program which will find factors of given number and find whether the factor is even or odd.
Hint: Use Loop with if-else statements
about program : this code will try inputs and valuate for integer and loop until we input integer not float
"""

# wrapping in true statement and try to get the value and evaluate it
while True:
    try:
        en = int(input("Enter integer only: "))
# evaluating the input and use if and else for even and odd number segregation
        if (en % 2) == 0:
            print("{0} is Even".format(en))
        else:
            print("{0} is Odd".format(en))
# break the loop for try to exit
        break
# except make output for other inputs with error information and continue until getting the integer
    except ValueError:
        print("please input integer only")
        continue
