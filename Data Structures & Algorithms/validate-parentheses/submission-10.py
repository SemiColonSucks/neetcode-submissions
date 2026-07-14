class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)<2:
            return False
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==')' and stack and stack[-1]=='(':
                stack.pop()
            elif i==']' and stack and stack[-1]=='[':
                stack.pop()
            elif i=='}' and stack and stack[-1]=='{':
                stack.pop()
            elif len(stack)==0 and (i in [')','}',']']):
                return False
            else:
                return False
                
        if len(stack)==0:
            return True
        return False