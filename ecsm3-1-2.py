"""
2. Data of XYZ company is stored in sorted list. Write a program for searching
specific data from that list.
Hint: Use if/elif to deal with conditions.

"""
xyz_va = (
	'Aarumugam', "Balan", "Chatan", "Paanan", "Evvi", "Gugan", "valli", "azhagi", "Thamizhi", "Murasu", "Vaazh",
	"Karuppu",
	"Kaathaan", "Sevvi", "Mozhi", "Udai", "Velan", "Velan", "yaazhi", "iraivi", "murugan", "naavi", "ooraan",
	"pothigan")

va = sorted(xyz_va)

n = str(input("Enter the number to be searched : "))
if n in va:
	print("Item found at the Position : ", va.index(n) + +1)
	for i, each in enumerate(va, start=1):
		print("{}.{}".format(i, each))

else:
	print("Item not found in list")
