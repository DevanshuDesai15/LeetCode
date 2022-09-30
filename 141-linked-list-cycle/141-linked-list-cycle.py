# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:# we shifting fast by 2 there should not be a Null at end
            slow = slow.next # shift 1
            fast = fast.next.next # shift 2
            if slow == fast:
                return True
        return False 