class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1
        sort_hm=sorted(hm.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sort_hm[i][0])
        return res
                
                


            

        