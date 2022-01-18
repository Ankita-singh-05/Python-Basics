# Return statement is used to end the execution of the function call and returns the result


def cube(num):
    c = num * num * num
    return c
    # when we write return it breaks out of the function and will not print further statements
    # print("code")

result = cube(4)
print(cube(3))
print(result)