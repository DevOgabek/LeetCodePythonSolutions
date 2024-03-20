# Cells in a Range on an Excel Sheet

class Solution(object):
    def cellsInRange(self, s):
        start, start_char = int(s[1]), ord(s[0])
        end, end_char = int(s[-1]) + 1, ord(s[3]) + 1
        arr = []
        
        for i in range(start_char, end_char):
            for j in range(start, end):
                arr.append(chr(i) + str(j))
                
        return arr
    
solution = Solution()
print(solution.cellsInRange("K1:L2"))