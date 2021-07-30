Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]




class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        c1 = Counter(l1)
        c2 = Counter(l2)
        res = []
        for i in l1:
            if(i not in l2 and c1[i]==1):
                res.append(i)
        for i in l2:
            if(i not in l1 and c2[i]==1):
                res.append(i)
        return res
      
o=[]
s=s1+" "+s2
sl=s.split(" ")
for w in sl:
    if sl.count(w)==1:
        o.append(w)
return o


def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        x = A.split(" ")
        y = B.split(" ")
        
        result = []
        # concatenate the A and B words in list
        for elem in x:
            result.append(elem)
            
        for elem in y:
            result.append(elem)
        
        # return the uncommon words i.e. words which repeated 1 time into concatenated list
        answer = []
        for res in result:
            if result.count(res) == 1:
                answer.append(res)
        return answer
