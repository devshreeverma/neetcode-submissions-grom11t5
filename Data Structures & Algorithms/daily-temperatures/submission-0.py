class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        ans=[0]*(len(temperatures))
        i=0
        res=0
        for i in range(len(temperatures)):
            while len(s)>0 and temperatures[i]>temperatures[s[-1]]:
                res=s.pop()
                ans[res]=i-res

            s.append(i)
        return ans
