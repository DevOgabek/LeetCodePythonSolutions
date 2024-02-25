# Find the Town Judge

class Solution(object):
    def findJudge(self, n, trust):

        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for a in trust:
            out_degree[a[0]] += 1
            in_degree[a[1]] += 1
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        return -1

test = Solution()
print(test.findJudge(2, [[1,2]]))