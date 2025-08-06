class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        majority_count = len(nums) // 2
        for i in nums:
            table[i] = table.get(i, 0) + 1
            if table[i] > majority_count:
                return i

        