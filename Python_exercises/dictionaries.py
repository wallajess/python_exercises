# Creating a dictionary
a_dict ={"a": 1, "b": 2, "c": 3}


# Iterating over keys
for key in a_dict:
    print(key)

# Accessing the value to a specific key:
for key in a_dict:
    print(key, "->", a_dict[key]) # Dictionary_name[key] will access values

# Iterating over the values:
for x in a_dict.values():
    print(x * 2)

# To get all the values
nums = set(a_dict.values())
print(nums)

#


    