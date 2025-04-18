def sortThis(arr):

    # how many sub arrays are sorted?

    ans = 0
    for i in range(len(arr)):
        if i + 1 < len(arr) and arr[i] + 1 == arr[i + 1]:
            continue
        ans += 1
    return ans


print(sortThis([5, 3, 4, 1, 2]))  # output 3
"""
1 . [5, 3, 4, 1, 2]
arr[0] = 5
arr[0] + 1 = 6
"""
