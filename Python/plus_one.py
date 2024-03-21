# Plus One

class Solution(object):
    def plusOne(self, digits):
        total = str(int(int(''.join(map(str, digits)))) + 1)
        return [int(num) for num in total]
    
solution = Solution()
print(solution.plusOne([1,2,3]))