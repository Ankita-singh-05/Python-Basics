
# \n -- it is used to print on next line
print("Bear \nAcademy")

# \" -- escape character -- to print quotation mark
print("Bear \" Academy")

# we can also create the string
phrase = "Giraffe Academy"
print(phrase)

# Concatenation --> Appending one string from another string
print(phrase + " is cool")

# lower function converts the string to lowercase
print(phrase.lower())

# upper function converts the string to uppercase
print(phrase.upper())

# capitalize converts the first letter of the string to uppercase and rest lowercase
print(phrase.capitalize())

print(phrase.upper().isupper())

# To find the length of the string -- how many characters in the string
print(len(phrase))

# To access the first letter of the string
print(phrase[0])

# index function will return the index value of the string
print(phrase.index("G"))
print(phrase.index("a"))
# print(phrase.index("z"))  -- VALUEERROR -- substring not found

# it will replace the giraffer with elephant
print(phrase.replace("Giraffe", "Elephant"))