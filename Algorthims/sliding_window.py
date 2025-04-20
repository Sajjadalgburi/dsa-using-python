from typing import List


# Sliding Window of fixed size
def best_total_price(prices: List[int], k: int):
    total = sum(prices[:k])
    maxTotal = total

    for i in range(len(prices) - k):
        total -= prices[i]
        total += prices[i+k]
        maxTotal = max(maxTotal, total)

    return maxTotal

# print(best_total_price([100, 200, 300, 4, 2, 600], 2))

# Sliding Window of variable size


def longestSubArr(arr: List[int], sum: int):
    l, cur = -1, 0
    longest = 0
    for r in range(len(arr)):
        cur += arr[r]
        while cur >= sum:
            l += 1
            cur -= a[l]
        longest = max(longest, r - l)

    return longest


a = [4, 5, 2, 0, 1, 8, 12, 3, 6, 9]
print(longestSubArr(a, 15))

# find the longest sub array with the sum being less then s -> s = 15
