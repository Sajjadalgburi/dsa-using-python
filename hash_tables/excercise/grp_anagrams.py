def group_anagrams(arr: list[str]) -> list[list[str]]:
    my_dict = {}

    for word in arr:
        sorted_word = ''.join(sorted(word))

        if sorted_word in my_dict:
            my_dict[sorted_word].append(word)
        else:
            my_dict[sorted_word] = [word]

    return list(my_dict.values())


# Test cases
print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(
    ["listen", "silent", "triangle", "integral", "garden", "ranged"]))
