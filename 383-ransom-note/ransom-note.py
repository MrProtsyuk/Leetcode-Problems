class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}

        for char in magazine:
            if char in magazine_letters:
                magazine_letters[char] += 1
            else:
                magazine_letters[char] = 1

        for char in ransomNote:
            if char not in magazine_letters or magazine_letters[char] == 0:
                return False
            magazine_letters[char] -= 1
        return True
        