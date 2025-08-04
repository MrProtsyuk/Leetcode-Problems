class Solution:
    def isPalindrome(self, x: int) -> bool:
        compareArr = []
        arr = list(str(x))
        for i in range(1, len(arr) + 1):
            compareArr.append(arr[-i])

        compareStr = "".join(compareArr)
        if str(x) == compareStr:
            return True
        else:
            return False