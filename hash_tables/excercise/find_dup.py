"""
appearance = []
my_dict = {} // (n)

Keep track of how many times each numeric value appears
for the values that appear more than once, > 1
append that into a temporary list that will be returned
"""


def find_duplicates(arr):
    appearance = []
    my_dict = {}

    for val in arr:
        if val in my_dict:
            my_dict[val] += 1
            if my_dict[val] == 2:
                appearance.append(val)
        else:
            my_dict[val] = 1

    return appearance


print(find_duplicates([1, 2, 3, 4, 5]))  # []
print(find_duplicates([1, 1, 2, 2, 3]))  # [1, 2]
print(find_duplicates([1, 1, 1, 1, 1]))  # [1]
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
