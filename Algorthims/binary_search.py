from typing import List


def binary(arr: List[int], target: int) -> int | None:
    if not arr:
        return None

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = round((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return None


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary(a, 7))  # returns the index
