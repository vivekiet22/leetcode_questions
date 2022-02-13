# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr :
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        head= l1
        prev = None
        c = 0
        sum = 0
        
        while l1 is not None and l2 is not None:
            sum = c+l1.val+l2.val
            l1.val = sum%10
            c = int(sum/10)
            prev = l1
            l1 = l1.next 
            l2 = l2.next
        if l1 is not None or l2 is not None:
            if l2 is not None:
                prev.next = l2
            l1 = prev.next 
            while l1 is not None:
                sum = c+l1.val
                l1.val = sum%10
                c = int(sum/10)
                prev = l1
                l1 = l1.next
                
        if c>0:
            prev.next = ListNode(c)
        return reverse(head)
                

        
