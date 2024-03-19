# Minimum Deletions to Make String K-Special

class Solution(object):
    def minimumDeletions(self, word, k):
        hash_map = {}
        
        for i in word :
            hash_map[i] = hash_map.get(i , 0)+1
            
        l = sorted(list(hash_map.values()) , reverse = True)
        min_deletions = float("inf")
        
        for i in range(len(l)):
            t = l[i]
            deletions = 0
            for j in range(len(l)):
                if l[j] > t+k :
                    deletions += (l[j] - (t+k))
                elif l[j] < t :
                    deletions += l[j]
            min_deletions = min(min_deletions , deletions)
            
        return min_deletions
    
solution = Solution()
print(solution.minimumDeletions())