# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (head == None):
            return False
        l1 = head
        l2 = head   


        while(True):
            l1 = l1.next
            
            if(l2.next == None):
                return False
            l2 = l2.next.next

            if(l1 == None or l2 == None):
                return False
            
            if(l1 == l2):
                return True