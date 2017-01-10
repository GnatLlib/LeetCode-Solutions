'''
	LeetCode Problem 2. Add two numbers
	You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
	
	You may assume the two numbers do not contain any leading zero, except the number 0 itself.
	'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        temp = head
        carry = False
        while l1 or l2 or carry:
            temp.next = ListNode(0)
            temp = temp.next
            
            if carry:
                temp.val = temp.val + 1
            carry = False
            
            if l1 and not l2:
                temp.val = temp.val + l1.val
                l1 = l1.next
            
            elif l2 and not l1:
                temp.val = temp.val + l2.val
                l2 = l2.next
            elif l2 and l1:
                temp.val = temp.val + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            else:
                continue
            
            if temp.val >= 10:
                temp.val = temp.val-10
                carry = True
        return head.next
            