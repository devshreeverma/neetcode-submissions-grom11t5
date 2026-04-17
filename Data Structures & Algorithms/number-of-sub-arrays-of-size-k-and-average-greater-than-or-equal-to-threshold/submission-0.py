class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        ans=0
        curr_sum=0
        for r in range(len(arr)):
            curr_sum+=arr[r]
            if r-l+1>k:
                curr_sum-=arr[l]
                l+=1
            if r-l+1==k:
                if curr_sum>=k*threshold:
                    ans+=1
        return ans