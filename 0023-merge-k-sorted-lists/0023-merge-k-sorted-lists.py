# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def fun(l1,l2):
            dummy = ListNode()
            res = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    dummy.next = ListNode(l2.val)
                    l2 = l2.next
                dummy = dummy.next
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            return res.next

        merge = None
        for i in range(len(lists)):
            merge = fun(merge,lists[i])
        
        return merge
                

        