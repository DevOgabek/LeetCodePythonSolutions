# Check if Number Has Equal Digit Count and Digit Value

class Solution(object):
    def digitCount(self, num):
        n = len(num)
        
        for i in range(n):
            digit = int(num[i])
            count = num.count(str(i))
            
            if count != digit:
                return False
        
        return True
    
solution = Solution()
print(solution.digitCount("1210"))