class Solution:
    def hasSameDigits(self, s: str) -> bool:
        output = ""
        for i in range(len(s) - 1):
            val = (int(s[i]) + int(s[i+1])) % 10
            output += str(val)
        
        if len(output) > 2:
            return self.hasSameDigits(output)
        else:
            if output[0] == output[1]:
                return True
            else:
                return False
