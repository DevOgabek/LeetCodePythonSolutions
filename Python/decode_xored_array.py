# Decode XORed Array

class Solution(object):
    def decode(self, encoded, first):
        decoded_array = [first]
        for num in encoded:
            decoded_array.append(decoded_array[-1] ^ num)
        return decoded_array

test = Solution()
print(test.decode([1, 2, 3, 4, 5]))