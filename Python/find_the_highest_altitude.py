# Find the Highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        _sum = 0
        highest_altitude = 0
        for num in gain:
            _sum += num
            highest_altitude = max(_sum, highest_altitude)
        return highest_altitude

test = Solution()
print(test.largestAltitude([-5,1,5,0,-7]))