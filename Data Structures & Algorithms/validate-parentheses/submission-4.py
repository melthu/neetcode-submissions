class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through string
        # if open bracket add to stack
        # if close bracket check if corresponding open bracket is at top of stack
        # if it is, pop top of stack
        # if it is not, return False

        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        for i in range(len(s)):
            if s[i] in closeToOpen.values():
                stack.append(s[i])
            else:
                if (stack and stack[-1] == closeToOpen[s[i]]):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        