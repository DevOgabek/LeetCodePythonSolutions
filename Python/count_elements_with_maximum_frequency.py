# Count Elements With Maximum Frequency

from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        freq_counter = Counter(nums)
        print(freq_counter)
        
        max_frequency = max(freq_counter.values())

        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]

        total_frequency = max_frequency * len(max_freq_elements)

        return total_frequency

solution = Solution()
print(solution.maxFrequencyElements([1,2,2,3,1,4]))