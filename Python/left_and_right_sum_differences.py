# Left and Right Sum Differences

class Solution(object):
    def leftRightDifference(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            total_sum -=num
            answer.append(abs(left_sum - total_sum))
            left_sum += num

        return answer

test = Solution()
print(test.leftRightDifference([10,4,8,3]))