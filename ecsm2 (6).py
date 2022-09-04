"""
eureka-Python Assignment
2. Write a code which accepts a sequence of words as input and prints the words in a
sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

about program : simple answer from the user and split the word in the sequence num caps small
"""
# getting input from person as answer for a question
quest = input("how are you feeling today?: ")
# break it into words by space from sentence answered
txt = quest.split()
# sort the list in the words provided
txt.sort()
# display the sorted words
for word in txt:
    print(word)
