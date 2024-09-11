# 2. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
first_name = input("Enter Your First Name : ")
last_name = input("Enter Your Last Name : ")

def reverse(name):
    reverse_name = ""
    for word in name:
        reverse_name = word+reverse_name
    return reverse_name
first_reverse = reverse(first_name)
last_reverse = reverse(last_name)

print("Reverse : "+first_reverse+" "+last_reverse)