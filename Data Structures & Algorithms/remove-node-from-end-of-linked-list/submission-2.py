# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        LIST_SIZE = 0

        temp = head

        while(temp != None):
            temp = temp.next

            LIST_SIZE += 1
        
        if(LIST_SIZE <= 1):
            if(LIST_SIZE == 1):
                head = None
            return head


        if(n == LIST_SIZE):
            #Deletion at head
            temp = head.next
            del head
            head = temp

        
        else:

            Deleting_Node = LIST_SIZE - n 
            temp = head
            for i in range(Deleting_Node - 1):
                temp = temp.next
            
            Node_before = temp
            Node = temp.next

            Node_before.next = Node.next

            del Node

        return head


        
