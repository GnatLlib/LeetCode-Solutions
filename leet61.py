'''
	LeetCode Problem 61. Rotate ListNode
	Given a list, rotate the list to the right by k places, where k is non-negative
	
	'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        
        
        if length<=1 or k % length == 0:
            return head
        k = length - (k%length)
        
        curr = head
        for i in range(k):
            prev, curr= curr, curr.next
        
        newHead = curr
        prev.next = None
        
        while curr.next:
            curr = curr.next
        curr.next = head
        
        return newHead