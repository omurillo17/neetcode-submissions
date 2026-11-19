# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sig = head 
        ant = head

        while sig and sig.next:
            sig = sig.next
            sig = sig.next
            ant = ant.next

            if sig == ant:
                return True
        return False