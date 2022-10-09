# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        count = 0
        itr = head
        while itr != None:
            count += 1
            itr = itr.next
        itr = head
        count //= 2
        for i in range(count):
            itr = itr.next
        return itr
