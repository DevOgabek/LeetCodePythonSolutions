# Sort the People

class Solution(object):
    def sortPeople(self, names, heights):
        dic = {}
        for name, height in zip(names, heights):
            dic[height] = name
        sorted_heights = sorted(list(dic.keys()), reverse=True)
        return [dic[height] for height in sorted_heights]

test = Solution()
print(test.sortPeople(["Mary","John","Emma"], [180,165,170]))