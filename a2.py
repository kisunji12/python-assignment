# 2. Write a Python program to sort a given dictionary by values.
# Example: {'x':'c', 'y':'b', 'z':'a'} => {'x':'a', 'y':'b', 'z':'c'}

from typing import OrderedDict


letters = {'x': 'c', 'y': 'b', 'z': 'a'}
sorted_keys = sorted(letters.keys())
sorted_values = sorted(letters.values())

# sorted() ->  sorted function actually need 3 arguments
#  1. object -> iterabels  2. key  3. reverse

sorted_dict = dict(zip(sorted_keys, sorted_values))

# zip function is used to add two list or tuple to map each other

print(sorted_dict)
