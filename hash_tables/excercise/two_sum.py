def two_sum(arr: list[int], target: int):
    matching = []

    # Sort the array to use the two-pointer approach
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:  # Use left < right to avoid an infinite loop
        if arr[left] + arr[right] == target:
            matching.append([arr[left], arr[right]])  # Append as a list
            left += 1  # Correctly increment left
            right -= 1  # Correctly decrement right
        elif arr[left] + arr[right] < target:
            left += 1  # Move left pointer to the right
        else:
            right -= 1  # Move right pointer to the left

    return matching


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))
