# Dictories is used to store the value in Key-Values pair

# We can even write numbers as a Key but it should be unique

monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

# Accessing the values from the dictionary

print(monthConversions["Jan"])
print(monthConversions["Jul"])

# Another way to access the value
print(monthConversions.get("Oct"))

# To print default value when no key matches otherwise it will print None
print(monthConversions.get("Krish", "Ooopps! This is not a valid key."))