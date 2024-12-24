# LİST

x = ["Abdurrahman", "Ömer", "Ozan", "Ege"]

# List are stored multiple items
# List items are ordered, changeable, and allow duplicate
# list items are indexed, first item index is 0

# I want to call ömer
print(x[1])
# I want to call ege
print(x[3])

print(len(x)) # shows how many items in the list

# List items can be of any data type
list1 = ["Abdurrahman", "Ömer", "Ozan", "Ege"] # str
list2 = [4, 5, 6, 7, 8] # int
list3 = [True, False, False] # boolean

# list() constructor
list4 = list(("Abdurrahman", "Ömer", "Ozan", "Ege"))
print(list4)

# negative indexing
list1 = ["Abdurrahman", "Ömer", "Ozan", "Ege"]
list1[-1]

list5 = ["Abdurrahman", "Ömer", "Ozan", "Ege","Mete","Eren"]
print(list5[2:5])
# the search will start at index 2 (included), and end at index 5 (excluded)
# index start with 0

list5 = ["Abdurrahman", "Ömer", "Ozan", "Ege","Mete","Eren"]
if "Ömer" in list5:
    print("yes, 'Ömer' in the list")

################
# Python Collection (Arrays)
###############
# There are four collection data type
# List is collection which is ordered and changeable. Allow dublicates
# Tuple is collection which is ordered and unchangeable. Allow dublicates

# Changing datas
list6 = ["Abdurrahman", "Ömer", "Ozan", "Ege","Mete","Eren"]
list6[0] = "Rana"
print(list6)

# example
list6 = ["Abdurrahman", "Ömer", "Ozan", "Ege","Mete","Eren"]
list6[1:2] = ["Mustafa", "Yusuf"]
print(list6)

list6 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
list6[1:4] = ["Abdurahman"]
print(list6)

# insert() method
list7 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
list7.insert(2, "Abdurahman")
print(list7)

list7 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
list7.insert(3, "Melike Rana")
print(list7)

list7 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
list7.append("Melike Rana")
print(list7)

list8 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
list9 = ["Melon", "Avacado"]
list8.extend(list9)
print(list8)

list8 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
mytuple = ("Melon", "Avacado")
list8.extend(mytuple)
print(list8)

list7 = ["Abdurrahman", "Ömer", "Ozan", "Ege","Mete","Eren"]
list7.remove("Abdurrahman")
print(list7)