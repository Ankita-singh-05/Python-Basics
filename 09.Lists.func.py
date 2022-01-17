lucky_numbers = [4 , 6, 27, 23, 43]
friends = ["Kalyani", "Kalyani", "Shivani", "Geeta", "Shraddha", "Muskan"]

# EXTEND METHOD
# it will extend the list by adding other list
friends.extend(lucky_numbers)
print(friends)

# SORT
# it will sort the list in ascending order
# it will only sort the string list or the number list but not together
print(friends.sort()) 

lucky_numbers.sort()
print(lucky_numbers)

# REVERSE
# it will reverse the order of the list
lucky_numbers.reverse()
print(lucky_numbers)

# APPEND
# it will add the elements to the end of the list
friends.append("Krishna")
print(friends)

# INSERT
# it will take two argument index value where u want to insert the element or item and elemnt name 
friends.insert(1, "Kanha")
print(friends)

# REMOVE
# used to remove the elments
friends.remove("Kanha")
print(friends)

# To check how many time the element is present in the list
friends.count("Kalyani")
print(friends)

# POP -- Used to remove the last element
friends.pop()
print(friends)

# To check that element is present in the list or not
print(friends.index("Kalyani"))
# it willthrow an error if the element is not presesnt in the list
print(friends.index("Mike"))  #ValueError : "Mike" is not in the list

# CLEAR
# to remove all the elements from the list
friends.clear()
print(friends)  # it will return an empty list

# COPY
# copying the list 
friends2 = friends.copy()
print(friends2)