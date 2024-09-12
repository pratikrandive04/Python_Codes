# 6. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
number = int(input("Enter Your Number : "))

n=number
nn=int(f"{number}{number}")
nnn=int(f"{number}{number}{number}")

sum_of_number = n+nn+nnn
print("n+nn+nnn : ",sum_of_number)