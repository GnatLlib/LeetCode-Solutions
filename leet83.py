'''
	LeetCode 83. Remove Duplicates from Sorted List
	'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = head
        temp = head.next
        while temp:
            if temp.val == prev.val:
                prev.next=temp.next
                
            
            else:
                prev = temp
            temp = temp.next
        return head