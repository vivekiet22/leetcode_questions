# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def length(head):
    k = 0
    temp = head 
    while temp:
        k+=1 
        temp = temp.next
    return k
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        prev = next = None
        curr = head
        count = 0
        n = length(head)
        print(n)
        while curr is not None and count<k:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
            count+=1
            
        if next is not None and n-k >=k:
            print("done")
            head.next = self.reverseKGroup(next,k)
        else:
            head.next = next
        return prev
        
