# Sort Integers by The Number of 1 Bits

class Solution(object):
    def sortByBits(self, arr):
        def count_ones(num):
            return bin(num).count('1'), num

        arr.sort(key=count_ones)
        
        return arr

solution = Solution()
print(solution.sortByBits([0,1,2,3,4,5,6,7,8]))