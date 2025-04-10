"""

1. using a dict i will keep track of each occurance of a letter
{
    l: 1,
    e: 3,
    t: 1,
    c: 1,
    o: 1,
    d: 1,
}

2. i will use a for loop to iterate over each char in the word
3. i will perform a check to see if that given char is in the my_dict[char] = 1
4. return the char in the for loop
5. other wise, exist the for loop by returning None

"""


def first_non_repeating_char(word):
    my_dict = {}

    for char in word:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    for letter in word:
        if my_dict[letter] == 1:
            return letter

    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
