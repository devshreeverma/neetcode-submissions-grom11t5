class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref=[0]*len(nums)
        i=1
        suff=[0]*len(nums)
        j=len(nums)-2
        suff[len(nums)-1]=nums[len(nums)-1]
        pref[0]=nums[0]
        while j>=0:
            suff[j]=nums[j]+suff[j+1]
            j-=1
        for i in range(len(nums)):
            pref[i]=pref[i-1]+nums[i]
        for i in range(len(nums)):
            left = pref[i-1] if i>0 else 0
            right = suff[i+1] if i<len(nums)-1 else 0

            if left == right:
                return i
        return -1