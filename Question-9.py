# Write a python script to use NOT IN operator to display data the not present in the list 

data_list = [23,43,46,65,67,78,67,56,67,897,67,4,243,243,56,67,56,3,43,54,56,43,243,67,78,54,54,978,54,65,65,65,98,65,65,35,65,54,21,21,32,65,65,98,98,87,54,21,21,32,20,20,21,32,3253,35,56,68,89,35,.2,21,54,68,96,63,2,41,57,86,6,]

value = int(input("Enter a value: "))

result = value not in data_list

print(result)

print()