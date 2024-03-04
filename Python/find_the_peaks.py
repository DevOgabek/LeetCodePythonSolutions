# Find the Peaks

class Solution(object):
    def findPeaks(self, mountain):
        peaks = []
        n = len(mountain)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks  

solution = Solution()
print(solution.findPeaks([2,4,4]))