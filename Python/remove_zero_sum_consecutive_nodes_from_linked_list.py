# Remove Zero Sum Consecutive Nodes from Linked List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

result = solution.removeZeroSumSublists(head)

while result:
    print(result.val, end=" -> ")
    result = result.next