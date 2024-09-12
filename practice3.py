# 3. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

list_numbers = "1,2,3,4,5,6"

List = list_numbers.split(",")

Tuple = tuple(List)

print("List : ",List)
print("Tuple : ",Tuple)