/**
	LeetCode Question 24
	Swap Nodes in Pairs
	
	Given a linked list, swap every two adjacent nodes and return its head.
	

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        
       if(head==NULL||head->next==NULL)
       {
           return head;
       }
       else
       {
           ListNode* next = head->next;
           ListNode* nextnext = next->next;
           next->next = head;
           head->next = swapPairs(nextnext);
           return next;
       }
      
       
    }
};