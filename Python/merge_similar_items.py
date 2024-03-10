# Merge Similar Items

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        value_weights = {}
        items = items1 + items2
        for item in items:
            value = item[0]
            weight = item[1]
            if value not in value_weights:
                value_weights[value] = 0
            value_weights[value] += weight
        
        sorted_values = sorted(value_weights.items())
        ret = [[value, weight] for value, weight in sorted_values]
    
        return ret

solution = Solution()
print(solution.mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))