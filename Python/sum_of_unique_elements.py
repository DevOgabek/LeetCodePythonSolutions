# Sum of Unique Elements

class Solution(object):
    def sumOfUnique(self, nums):
        count = {}
        unique_sum = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            if freq == 1:
                unique_sum += num

        return unique_sum

solution = Solution()
print(solution.sumOfUnique([1,2,3,2]))