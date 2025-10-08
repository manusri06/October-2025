# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy
        dummy.next = head

        curr = dummy.next
        for i in range(n):
            curr = curr.next
    
        while curr:
            curr = curr.next
            dummy = dummy.next
        dummy.next = dummy.next.next

        return res.next



        