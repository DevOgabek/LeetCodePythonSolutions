# Truncate Sentence

class Solution(object):
    def truncateSentence(self, s, k):
        return ''.join([word + ' ' for word in s.split(' ')[:k]])[:-1]
 
test = Solution()
print(test.truncateSentence("Hello how are you Contestant", 4))