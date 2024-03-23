# Maximum 69 Number

class Solution(object):
    def maximum69Number (self, num):
        k, i = 0, 1

        while i < num:
            if num // i % 10 == 6:
                k = i
            i *= 10

        return num + 3 * k
    
solution = Solution()
print(solution.maximum69Number(9669))