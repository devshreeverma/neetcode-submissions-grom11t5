class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one=0
        maxone=0
        for i in range(len(nums)):
            if nums[i]==1:
                one+=1
            else:
                if one > maxone:
                    maxone = one
                one=0
        if maxone>one:
            return maxone
        else:
            return one