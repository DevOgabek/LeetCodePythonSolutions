# Greatest Common Divisor Traversal

class Solution(object):
    def canTraverseAllPairs(self, nums):
        num_elements = len(nums)
        
        if num_elements == 1:
            return True
        
        disjoint_set = [_ for _ in range(num_elements)]
        

        set_size = [1] * num_elements
        
        factor_first_occurrence = {}
        
        def find_set_leader(x):
            if disjoint_set[x] == x:
                return x
            disjoint_set[x] = find_set_leader(disjoint_set[x])
            return disjoint_set[x]
        
        def union_sets(x, y):
            x_leader, y_leader = find_set_leader(x), find_set_leader(y)
            if x_leader == y_leader:
                return
            if set_size[x_leader] < set_size[y_leader]:
                x_leader, y_leader = y_leader, x_leader
            disjoint_set[y_leader] = x_leader
            set_size[x_leader] += set_size[y_leader]
        
        for i in range(num_elements):
            num = nums[i]
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if divisor in factor_first_occurrence:
                        union_sets(i, factor_first_occurrence[divisor])
                    else:
                        factor_first_occurrence[divisor] = i
                    while num % divisor == 0:
                        num //= divisor
                divisor += 1
            if num > 1:
                if num in factor_first_occurrence:
                    union_sets(i, factor_first_occurrence[num])
                else:
                    factor_first_occurrence[num] = i
        
        return set_size[find_set_leader(0)] == num_elements

test = Solution()
print(test.canTraverseAllPairs([2,3,6]))