class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(s.lower().split(" "))
        string=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                string+=s[i]
        s=string[:]
        return s==s[::-1]