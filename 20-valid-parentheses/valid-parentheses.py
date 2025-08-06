class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
        
        return not stack