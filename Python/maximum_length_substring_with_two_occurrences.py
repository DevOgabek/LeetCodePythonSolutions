# Maximum Length Substring With Two Occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mpp = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            if s[r] in mpp:
                mpp[s[r]] += 1
                while mpp[s[r]] > 2:
                    mpp[s[l]] -= 1
                    if mpp[s[l]] == 0:
                        del mpp[s[l]]
                    l += 1
            else:
                mpp[s[r]] = 1

            max_len = max(max_len, r - l + 1)

        return max_len
    
solution = Solution()
print(solution.maximumLengthSubstring("bcbbbcba"))