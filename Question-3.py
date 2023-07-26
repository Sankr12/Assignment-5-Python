# Write a python script to swap data of two variables

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

print("Before Swapping")
print("Var1 = ",a)
print("Var2 = ",b)
print()

a,b = b,a 

print("Afer Swapping")
print("Var1 = ",a)
print("Var2 = ",b)