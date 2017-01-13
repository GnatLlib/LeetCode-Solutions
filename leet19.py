'''
	LeetCode Problem 19. Remove Nth Node from End of Linked List

	'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
       
        temp = head
        prev = None
    
        while 1:
            temp2 = temp
            for i in range(n):
                temp2 = temp2.next
            if temp2 == None:
                if prev == None:
                    return temp.next
                prev.next = temp.next
                return head
        
            prev = temp
            temp = temp.next