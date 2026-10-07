# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        while curr:
            if curr.val != 1001:
                curr.val = 1001
                curr = curr.next
            else:
                return True
        
        return False

        