class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s.lower().split(" "))
        string=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                string+=s[i]
        print(string)

        l,r=0,len(string)-1
        while l<=r:
            if string[l]!=string[r]:
                return False
            l+=1
            r-=1
        return True
        