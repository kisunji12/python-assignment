# List
# Write a Python program to sum a specific column of a list in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists: 12
# Sum: 2nd column of the said list of lists: 15
# Sum: 4th column of the said list of lists: 9

l1 = [
    [1, 2, 3, 2],
    [4, 5, 6, 2],
    [7, 8, 9, 5]
]

l2 = list(map(sum, zip(*l1)))

print(l2)
