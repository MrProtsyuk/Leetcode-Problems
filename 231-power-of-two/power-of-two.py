import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        logarithm = int(math.log2(n))

        return pow(2, logarithm) == n