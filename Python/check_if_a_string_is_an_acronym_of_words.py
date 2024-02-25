# Check if a String Is an Acronym of Words

class Solution(object):
    def isAcronym(self, words, s):
        if len(s) != len(words):
            return False
        
        for i in range(len(words)):
            if s[i] != words[i][0]:
                return False
        
        return True

test = Solution()
print(test.isAcronym(["alice","bob","charlie"], "abc"))