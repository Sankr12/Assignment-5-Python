# Write a python script which takes a three digit number from the user and display its first digit only.

num = int(input("Enter a three digit Number: "))

num = num // 100

print("The first digit:",num)