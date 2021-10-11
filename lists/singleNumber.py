class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for key,value in dict.items():  # iterate through list of tuples
            if 1 == value:
                return key
