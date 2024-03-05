# Sorting the Sentence

class Solution(object):
    def sortSentence(self, s):
        shuffled_words = s.split()

        original_words = [word[:-1] for word in sorted(shuffled_words, key=lambda x: int(x[-1]))]

        reconstructed_sentence = ' '.join(original_words)

        return reconstructed_sentence

solution = Solution()
print(solution.sortSentence("is2 sentence4 This1 a3"))