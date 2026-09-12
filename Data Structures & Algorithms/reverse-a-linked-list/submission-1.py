# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if(head == None):
            return head

        a = head
        b = head.next
        head.next = None

        while (b != None):
            temp = b.next 

            b.next = a

            a = b

            b = temp
        return a
        





