Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
  

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        length = len(words)
        output = []
        for i in words[0]:
            check = True
            for j in range(1, length):
                if i in words[j] and check:
                    words[j] = words[j].replace(i, "", 1)
                    check = i
                else:
                    check = None
            if check == i:
                output.append(i)

        return output



class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # this will serve as the output array of letters
        common_Counts = []
        # Initializing a list that will collect dictionaries representing letter: count
        # pairs for each word
        temp_dicts = []
        
        # Part I: Creating and populating dicts of letter:count for each word
        for word in words:
            # Initializing of the dictionary of letter:count pairs for the current word
            temp_dict = {}

            # populating temp_dict
            for letter in word:
                if letter not in temp_dict:
                    temp_dict.update({letter: 1})
                else:
                    temp_dict[letter] += 1
            # appending temp_dict to the collector list, temp_Dicts, initialized above
            temp_dicts.append(temp_dict)

        # Part II: Once temp_dicts has collected the dicts for each word, we iterate 
        # over each letter, over that letter's occurrence in each dict.
        for letter in string.ascii_lowercase:
            # Initializing a variable to track the number of words that feature at least one
            # occurrence of the current letter being checked
            words_featuring = 0
            # Reading the bounds for this problem, it is observed that the maximum possible number of letters 
            # is words.length * words[i].length, whose upper bound comes out to 100 * 100  = 10,000.
            letter_count = 10_000

            for dict in temp_dicts:
                # To calculate the number of a particular letter that we should return in the output array,
                # we must first determine if that letter is indeed present in EVERY word
                if letter in dict:
                    # A cache is maintained of the minimum of the current letter count of the current word (as 
                    # represented by the current dictionary being iterated over), and the overall minimum.
                    letter_count = min(dict[letter], letter_count)
                    # we also must maintain a count of the number of words featuring the current letter being
                    # checked, using the variable initialized at the beginning of part II.
                    words_featuring += 1
            # A letter will only be returned in the output array if it is present at least once in each
            # word
            if words_featuring == len(words):
                # if the current letter is indeed present in every word, we add the number of that letter to the output
                # array equal to the FEWEST occurrences of that letter in any particular word
                common_Counts += [letter for count in range(letter_count)]
                
        return common_Counts
