# TRY & EXCEPT
# If we are taking input from the users in the integer and 
# they are passing the string value then it will throw an error
# So to avoid this we use Try and except
# In this case user will get the suggestion that inputformat is wrong
# and it will not directly end the program throwing an error



try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    # print("Divided by zero error")
    print(err)
except ValueError:
    print("Invalid input")

