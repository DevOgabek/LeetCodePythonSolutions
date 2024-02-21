# Final Value of Variable After Performing Operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for operation in operations:
            if operation[1] == "+":
                count += 1
            else:
                count -= 1
        return count

test = Solution()
print(test.finalValueAfterOperations(["--X","X++","X++"]))