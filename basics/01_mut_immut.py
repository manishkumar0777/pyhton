# mutable in python is means the actual data in the memory can be changed 
# -> List
# -> Set 
# -> Dictionary
# -> Bytearray
# -> Array



# immutable in python have a diffrent scene than other language here if the type is immuatble 
# it means the value in the memory cant be changed but if you look from diffrent perspective as variable 
# it can be changed because when you change the data of immytable types the refrence of the data gets changed 
# and you get the changed data.
# -> Integers
# -> Floating Point No.
# -> Boolean
# -> Strings
# -> Tuples
# -> Frozen set
# -> Bytes


# although its immutable its value get changed by changing the address referece
username = 'Manish'
print(username)

username = 'raunak'
print(username)

# another example with Integer
x=10
y=x
print(x,y)
x=16
print(x,y)

# here x refrence gets chaged to 16 but y still refering the 10 

