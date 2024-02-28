# Sort the People

class Solution(object):
    def sortPeople(self, names, heights):
        combined_data = list(zip(names, heights))

        sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)

        sorted_names = [name for name, _ in sorted_data]

        return sorted_names

test = Solution()
print(test.sortPeople(["Mary","John","Emma"], [180,165,170]))