# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # bring all non-val values to beginning, calculate length
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                # edit existing array
                k+=1
        return k
                
