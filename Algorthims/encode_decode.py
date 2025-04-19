from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        input:
        given array of strings

        output:
        single string with the decoded values

        1. I will iterate through every str in strings and break them apart
        for every encounter of a word, i will add an identirfieder to let me know
        that next to this is a differant word #


        test:
        iteration 1. we -> 2#we
        iteration 2. say -> 3#say
        iteration 3. : -> 1#:
        iteration 4. yes -> 3#yes
        output => "2#we3#say1#:3#yes"

        """

        output: str = ''

        for word in strs:
            word_length = len(word)  # lenght of the word

            # append into the ouput 1. lenght of the word,
            # followed by an identifier then the word itself
            new_word = f'{word_length}#{word}'
            output += new_word

        return output

    def decode(self, s: str) -> List[str]:
        """
        input:
        taken an a single encoded string

        output:
        an array of the decoded strings

        approach:
        iterate through the string 
        1. if we find a number we keep track of it
        2. once we reach a '#' we can then use the number to grab the char of the same length
        3. once found, then we append to the output array and return it at the end
        """

        output: List[str] = []

        for char in s:

            pass

        return output


s = Solution()

"""
Input: ["we","say",":","yes"]

after encode -> "2#we3#say1#:3#yes"
"""

decoded = s.encode(["we", "say", ":", "yes"])

print(decoded)  # output => "2#we3#say1#:3#yes"


"""
Input: "2#we3#say1#:3#yes" ["we","say",":","yes"]

after decode -> ["we","say",":","yes"]
"""
s.decode(decoded)
