# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        temp = head
        n = 0
        while(temp != None):
            temp = temp.next
            n += 1

        mid = n//2
        mid_head = head
        for _ in range(mid):
            mid_head = mid_head.next


        a = mid_head
        b = a.next
        mid_head.next = None
        while(b != None):
            temp = b.next
            b.next = a
            a = b
            b = temp

        reverse_mid_head = a
        ans = head

        for _ in range(mid):
            temp1 = head.next
            temp2 = reverse_mid_head.next


            if(temp1 == reverse_mid_head):
                break

            head.next = reverse_mid_head
            reverse_mid_head.next = temp1
            

            head = temp1
            reverse_mid_head = temp2

        head = ans



        