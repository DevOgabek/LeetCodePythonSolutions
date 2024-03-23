# Minimum Sum of Four Digit Number After Splitting Digits

class Solution(object):
    def minimumSum(self, num):
        digits = [int(d) for d in str(num)]
        
        digits.sort()
        
        part1 = 0
        part2 = 0
        
        for i in range(len(digits)):
            if i == 0 and digits[i] == 0:
                continue
            
            if i % 2 == 0:
                part1 = part1 * 10 + digits[i]
            else:
                part2 = part2 * 10 + digits[i]
        
        return part1 + part2
    
solution = Solution()
print(solution.minimumSum(2932))