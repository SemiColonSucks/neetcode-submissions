class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s.lower().split(" "))
        string=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                string+=s[i]
        s=string[:]
        l,r=0,len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        