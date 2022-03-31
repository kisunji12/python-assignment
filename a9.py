# Write a Python program to get the unique values in a given list of lists.
# Original list:
# [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Unique values of the said list of lists:
# [0, 1, 2, 3, 4, 5, 7]

l1 = [
    [1, 2, 3, 5],
    [2, 3, 5, 4],
    [0, 5, 4, 1],
    [3, 7, 2, 1],
    [1, 2, 1, 2]
]

# ul = []

# for l in l1:
#     for sl in l:
#         ul.append(sl)

# print(list(set(ul)))

result = {x for l in l1 for x in l}
print(list(result))
