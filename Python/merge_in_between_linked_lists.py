# Merge In Between Linked Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

list1 = ListNode(0)
current = list1
for i in range(1, 6):
    current.next = ListNode(i)
    current = current.next

list2 = ListNode(10)
current = list2
for i in range(11, 13):
    current.next = ListNode(i)
    current = current.next

print("Original list1:")
print_linked_list(list1)
print("Original list2:")
print_linked_list(list2)

sol = Solution()
merged_list = sol.mergeInBetween(list1, 2, 4, list2)

print("Merged list:")
print_linked_list(merged_list)