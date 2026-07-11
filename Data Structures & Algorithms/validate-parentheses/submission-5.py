class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        stack = []
        for c in s:
            if stack and self.isMatch(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True
        
    def isMatch(self, c1: str, c2: str) -> bool:
        if c1 == '(' and c2 == ')':
            return True
        elif c1 == '{' and c2 == '}':
            return True
        elif c1 == '[' and c2 == ']':
            return True
        else:
            return False


        
        