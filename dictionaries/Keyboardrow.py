Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm"


Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        keyboard_rows = {}
        # build the dictionary
        # mapping from letter -> which row on the keyboard the letter is on
        for letter in 'qwertyuiopQWERTYUIOP':
            keyboard_rows[letter] = 1
        for letter in 'asdfghjklASDFGHJKL':
            keyboard_rows[letter] = 2
        for letter in 'zxcvbnmZXCVBNM':
            keyboard_rows[letter] = 3
        for word in words:
            # find out which row the first letter of the word is on
            row = keyboard_rows[word[0]]
            # apply the lambda function to each letter in the word
            same_row_boolean_array = list(map(lambda x: keyboard_rows[x] == row, list(word)))
            # if all elements in the array are true then all
            # letters in the word were on the same row of the keyboard
            if all(same_row_boolean_array):
                ans += [word]
        return ans
