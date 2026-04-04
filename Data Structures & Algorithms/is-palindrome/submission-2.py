class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        charac=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        for c in s:
            if c not in charac:
                s=s.replace(c,"")

        y=s[::-1]
        if y==s:
            return True
        else:
            return False

