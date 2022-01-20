
# It will append the contents to the end of the file
employee_file = open("employees1.txt", "w")
# If we use "write" mode instead of append then it will overwrite the file

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file.close()

# We can create the file using filename
employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML File</p>")