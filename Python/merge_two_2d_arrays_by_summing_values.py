# Merge Two 2D Arrays by Summing Values

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        dic = {}
        
        for nums in [nums1, nums2]:
            for sublist in nums:
                id, val = sublist[0], sublist[1]
                dic[id] = dic.get(id, 0) + val
        
        return sorted(dic.items(), key=lambda x: x[0])
    
solution = Solution()
print(solution.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))