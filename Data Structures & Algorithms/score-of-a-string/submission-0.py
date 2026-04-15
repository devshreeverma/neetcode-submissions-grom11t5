class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        i=0
        j=1
        while i< (len(s)-1):
                ans+=abs(ord(s[j])-ord(s[i]))
                i+=1
                j+=1
        return ans