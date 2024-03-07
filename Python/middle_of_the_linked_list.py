# Middle of the Linked List

class Solution(object):
    def middleNode(self, head):
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer
    
solution = Solution()
print(solution.middleNode([1,2,3,4,5]))