class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        one_step = 2
        two_step = 1

        for i in range(3, n+1):
            current = one_step + two_step
            two_step = one_step
            one_step = current

        return one_step        
