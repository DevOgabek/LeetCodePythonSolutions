# Defanging an IP Address

class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

test = Solution()
print(test.defangIPaddr("1.1.1.1"))