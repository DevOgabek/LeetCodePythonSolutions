# Count Items Matching a Rule

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1
        return count

test = Solution()
print(test.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))