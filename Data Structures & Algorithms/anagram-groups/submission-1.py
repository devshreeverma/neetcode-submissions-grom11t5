class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        ans=[]
        for s in strs:
            key="".join(sorted(s))
            if key not in d:
                d[key]=[]
            d[key].append(s)

        for value in d.values():
            ans.append(value)
        return ans