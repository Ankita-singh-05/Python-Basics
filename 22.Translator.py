# Building a Translator

# Giraffe Language
# Vowels -> g ----> every vowels become g
# eg - dog -- dgg, cat -- cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))