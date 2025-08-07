class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        n = []
        for i in range(len(s)):
            if s[i] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                continue
            else:
                n.append(s[i])
        
        n = "".join(n)
        return n == n[::-1]