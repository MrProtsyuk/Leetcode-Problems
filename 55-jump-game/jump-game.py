class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sum = 0
        for i in nums:
            if sum < 0:
                return False
            elif i > sum:
                sum = i
            sum -= 1
        return True
            
        