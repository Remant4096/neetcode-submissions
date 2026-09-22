# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tempL1 = l1
        tempL2 = l2
        l3 = ListNode()
        tempL3 = l3
        L3_prev = None

        sum_digit = 0
        carry = 0
    
        def update_temp():
            nonlocal sum_digit,carry,tempL3,L3_prev
            if(sum_digit >= 10):
                carry = 1
                sum_digit = sum_digit - 10
            else:
                carry = 0
            
            tempL3.val = sum_digit
            tempL3.next = ListNode()
            L3_prev = tempL3
            tempL3 = tempL3.next
            

        while(tempL1 and tempL2):
            sum_digit = tempL1.val + tempL2.val + carry

            update_temp()

            tempL1 = tempL1.next
            tempL2 = tempL2.next

        
        while(tempL1):
            sum_digit = tempL1.val  + carry

            update_temp()
            
            tempL1 = tempL1.next
        

        while(tempL2):
            sum_digit = tempL2.val + carry

            update_temp()
            
            tempL2 = tempL2.next

        if(carry != 0):
            tempL3.val = carry
            tempL3.next = None
        else:
            del tempL3
            L3_prev.next = None

        return l3

