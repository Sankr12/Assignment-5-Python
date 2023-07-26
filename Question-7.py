# Write a python script which takes a three digit number from a user and display its last digit

num = int(input("Enter a three digit number: "))

num = num % 10

print("The middle digit:",num)