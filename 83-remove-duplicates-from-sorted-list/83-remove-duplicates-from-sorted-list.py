# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next == None:
                return head
    
            current = head.next
            prev = head
            while current != None:
                if prev.val == current.val:
                    prev.next = current.next
                else:
                    prev=current
                current = current.next
            return head
        return head