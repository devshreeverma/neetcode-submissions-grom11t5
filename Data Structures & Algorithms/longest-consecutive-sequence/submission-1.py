class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l=0
        nums.sort()
        maxn=nums[0]
        length=1
        max_length=1
        for r in range(1,len(nums)):
            if nums[r]==maxn:
                continue
            elif nums[r]==(maxn+1):
                length+=1
            else:
                length=1
                l=r
            max_length=max(max_length,length)
            maxn=nums[r]
        return max_length