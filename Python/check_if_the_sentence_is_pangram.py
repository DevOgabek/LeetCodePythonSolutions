# Check if the Sentence Is Pangram

class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26
    
solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))