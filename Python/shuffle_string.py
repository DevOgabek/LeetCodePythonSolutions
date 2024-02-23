# Shuffle String

class Solution(object):
    def restoreString(self, s, indices):
        shuffled = [''] * len(s)
        for i, char in zip(indices, s):
            shuffled[i] = char
        return ''.join(shuffled)

test = Solution()
print(test.restoreString("codeleet", [4,5,6,7,0,2,1,3]))