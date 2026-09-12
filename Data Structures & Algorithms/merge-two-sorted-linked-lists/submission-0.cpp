class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if(list1 == nullptr && list2 == nullptr)
            return nullptr;

        ListNode* list3 = new ListNode();
        ListNode* list3_head = list3;

        while(list1 != nullptr && list2 != nullptr){

            if(list1->val < list2->val){
                list3->val = list1->val;
                list1 = list1->next;
            }
            else{
                list3->val = list2->val;
                list2 = list2->next;
            }

            if(list1 != nullptr || list2 != nullptr){
                list3->next = new ListNode();
                list3 = list3->next;
            }
        }

        while(list1 != nullptr){

            list3->val = list1->val;
            list1 = list1->next;

            if(list1 != nullptr){
                list3->next = new ListNode();
                list3 = list3->next;
            }
        }

        while(list2 != nullptr){

            list3->val = list2->val;
            list2 = list2->next;

            if(list2 != nullptr){
                list3->next = new ListNode();
                list3 = list3->next;
            }
        }

        list3->next = nullptr;

        return list3_head;
    }
};