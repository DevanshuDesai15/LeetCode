# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        curr = dummy
        
        carry=0
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # addition for new value
            val = v1+v2+carry
            # for getting the carry if 7 +8 kinda example there
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val) # assigning the value to list
            
            # updating the pointer
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next