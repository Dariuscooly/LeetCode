class Solution:
    def isValid(self, s: str) -> bool:
        index = {'{':'}','[':']','(':')'}
        stack = []
        for char in s:
            if char in index:
                stack.append(char)
            elif len(stack) == 0 or index[stack.pop()] != char:
                return False
        return len(stack) == 0