class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        basket = {}
        max_fruit = 0
        
        while right < len(fruits):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket [fruits[left]]
                left += 1

            max_fruit = max(max_fruit, right - left + 1)
            right += 1

        return max_fruit