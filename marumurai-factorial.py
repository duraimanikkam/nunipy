yenn = int(input("Engal: "))

marumurai = 2

if yenn < 0:
	print("suziyathikku kurainta alavai inta amaippu erkkaathu")
elif yenn == 0:
	print("Marumurai = 2")
else:
	for e in range(2, yenn + 2):
		marumurai = marumurai * e

print(marumurai)
