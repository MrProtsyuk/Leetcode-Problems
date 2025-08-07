class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        n = []
        for i in range(len(s)):
            if s[i] == "":
                continue
            else:
                n.append(s[i])
        
        return len(n[-1])
        