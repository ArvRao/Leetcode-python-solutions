Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
Example 3:

Input: licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
Output: "husband"

Example 4:
Input: licensePlate = "OgEu755", words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
Output: "enough"
	
Example 5:

Input: licensePlate = "iMSlpe4", words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
Output: "simple"

def shortestCompletingWord(self, licensePlate, words):
        licensePlate=licensePlate.lower()
        map_={}
        arr=[]
        for i in licensePlate:
            if i.isalpha():
                if i not in map_:
                    map_[i]=1
                else:
                    map_[i]+=1
        for i, word in enumerate(words):
            count=0
            for key, value in map_.items():
                if word.count(key)>=value:
                    count+=1
            if count==len(map_):
                arr.append((word, len(word), i))
        arr=sorted(arr, key=lambda x:(x[1], x[2]))
        return arr[0][0]
        
        
#########
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
       #Step 1
	   d=dict()
        for i in licensePlate:
            if i.isalpha():
                d[i.lower()]=d.get(i.lower(),0)+1
        # print(d.items())
		#Step 2
        words.sort(key = len)
		#Step 3
        for index,word in enumerate(words):
            count=len(d)
            # print(word)
            dnew=dict()
			#Step 4
            for i in range(len(word)):
                dnew[word[i]]=dnew.get(word[i],0)+1
            # print(dnew.items())
			#Step 5
            for key,values in d.items():
                if key not in dnew:
                    break
                elif key in dnew:
                    if d[key]>dnew[key]:
                        break
                    else:
					#Step 6
                        count-=1
                        # print(count)
                        if count==0:
                            return word
		
Explanation :
Step 1: I create a dictionary for the original License plate, and add only those "i" in the dictionary that are alpha (NOT alnum - also adds numbers). I convert the alphabets into lower case using .lower().
Step 2 : I sort the words array in the increasing order of length (See Example 2 in the given testcases).
Step 3 : I then enumerate the sorted words array to find out the key , value pairs (index , word in this case). I then count the length of dictionary inside this loop each time as I am decrementing it later on...
Step 4 : I create a new dictionary (dnew) of each word inside the "words" array.
Step 5 : Then I run a loop over the "d" dictionary of the licenseplate, to check if the key is in dnew or not. If not, simply break and go for the next iteration in the words array. Else, if it is present, if d[key] i.e. the value of the dictionary is more than the available value in the word (Eg. - d={'c' = 4, 'r' = 5}, dnew={'c' = 2 , 'r' = 1}, then it will break and go over the next word.
Step 6 : If all the above conditions are not met, then that means that the key value pair satisfies the required statement, and now I can reduce the count by 1, ensuring that I have moved on to check the next key value pair. If I reach value of count = 0, then that means that I have checked each K,V pair and that the word is the correct answer to be returned.

P.S. - After reading through the solution, I hope you understand my explanation. Do upvote if you found it insightful and that this may help others to understand the problem. If you have any problem, make sure to drop by comments. I will respond back ASAP.

#############
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter([c.lower() for c in licensePlate if c.isalpha()])
        return min([(words[i], i) for i in range(len(words)) if not c-Counter(words[i])], key=lambda x: (len(x[0]), x[1]))[0]
