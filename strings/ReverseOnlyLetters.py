Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"



class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rev_str = list(filter(lambda x: x.isalpha(), s[::-1]))

        for idx, c in enumerate(s):
            if not c.isalpha():
                rev_str.insert(idx, c)
        
        return ''.join(rev_str)
      


def reverseOnlyLetters(self, S: str) -> str:
        newString = []
	
        S = list(S)
        tempS = S[::-1]

        for tS in tempS:
            if tS.isalpha():
                newString.append(tS)

        #print(f"tS: {newString}")

        for swi in range(len(S)):
            if S[swi].isalpha():
                pass
            else:
                temp = newString[swi:]
                newString = newString[:swi]
                newString.append(S[swi])
                newString.extend(temp)

        return "".join(newString)
      
      
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        s = ""
        for i in range(len(S)):
            if S[i].isalpha(): stack.append(S[i])
        for i in S:
            if not i.isalpha(): s += i
            else: s += stack.pop()
        return s
