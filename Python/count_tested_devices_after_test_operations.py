# Count Tested Devices After Test Operations

class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        count = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] > 0:
                count += 1
                for j in range(i+1, n):
                    batteryPercentages[j] -= 1
        return count

solution = Solution()
print(solution.countTestedDevices([1,1,2,1,3]))