class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_pos = 0
        y_pos = 0
        for i in moves:
            if i == "U":
                y_pos += 1
            elif i == "D":
                y_pos -= 1
            elif i == "L":
                x_pos -= 1
            elif i == "R":
                x_pos += 1

        return x_pos == 0 and y_pos ==0