/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
     ListNode* reverseList(ListNode* head) {

        ListNode *a = head;

        if(head == nullptr){
            return head;
        }


        ListNode *b = head-> next;
        head->next = nullptr;
        ListNode *temp = nullptr;
        while(b != nullptr){
            temp = b->next;
            b->next = a;
            a = b;
            b = temp;
        }

        return a;

    }

};
