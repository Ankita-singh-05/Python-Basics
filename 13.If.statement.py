

is_female = True
is_tall = False

if is_female:
    print("You are a female")
else:
    print("You are not a female")

# OR KEYWORD
if is_female or is_tall:
    print("You are a female or tall or both")
else:
    print("You neither female nor tall")

# AND KEYWORD
if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are not a female but are tall")
else:
    print("You are not a male and not tall")

    # NOT operator will return true if the condition is false 
    # and if True then it does not evaluates it to False