# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        sig = None
        actual = head

        while actual:
            sig = actual.next
            actual.next = prev
            prev = actual
            actual = sig 
        
        return prev
