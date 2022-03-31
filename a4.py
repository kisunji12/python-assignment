# Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

d1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}

# Using Dictionary Comprehension

# { <return k:v> <for (k,v) in iterables(keys, values, items)> <if condition if necessary>}

d2 = {k: v for (k, v) in d1.items() if v is not None}

print(d2)
