class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, direction = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                direction = 1
            elif idx == numRows - 1:
                direction = -1
            idx += direction

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return ''.join(rows)