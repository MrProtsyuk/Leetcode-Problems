class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for i in operations:
            if "++" in i:
                output = output + 1
            elif "--" in i:
                output = output - 1
            else:
                continue
        
        return output

        