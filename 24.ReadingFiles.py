
# reading files

# Reading the file -- will just read the file
employee_file = open("employees.txt", "r")

# if the file is readable the it will print True else False
print(employee_file.readable())

# To read the contents inside the file
print(employee_file.read())

# To read the individual line in the file
print(employee_file.readline())

for employee in employee_file.readlines():
    print(employee)

# to read all the lines inside the list
# print(employee_file.readlines())

# to print the specific line inside the list
# print(employee_file.readlines()[1])

# to close the file after reading it
employee_file.close()

# Write the file -- if want to modify the filw
# open("employees.txt", "w")

# Append the file -- if we want to append the information at the end of the file
# open("employees.txt", "a")

# Read and write the file
# open("employees.txt", "r+")