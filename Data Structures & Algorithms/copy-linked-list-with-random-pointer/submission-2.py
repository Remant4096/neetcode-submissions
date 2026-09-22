"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head ): # 'Optional[Node]'
        if(not head):
            return None

        temp = head
        New_head = Node(x=0)
        temp_new = New_head

        new_array_map = []
        hash_map = dict()
        i = 0

        while(temp):
            temp_new.val = temp.val
            hash_map[temp] = i
            new_array_map.append(temp_new) 

            temp = temp.next
            if(temp):
                temp_new.next = Node(x=0)
                temp_new = temp_new.next
            else:
                temp_new.next = None

            i += 1
        
        temp = head
        temp_new = New_head
        while(temp != None):
            if(temp.random == None):
                temp_new.random = None
            else:
                 temp_new.random =          new_array_map[hash_map[temp.random]]
            temp = temp.next
            temp_new = temp_new.next


        return New_head
        



        

        