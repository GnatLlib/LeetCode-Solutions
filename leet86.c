/**

	LeetCode Question 86.
	Partition ListNode
	Given a linked list and a value x, partition it such that all nodes less than
	x come before nodes greater than or equal to x.
	You should preserve the original relative order of the nodes of the two partitions.
	
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