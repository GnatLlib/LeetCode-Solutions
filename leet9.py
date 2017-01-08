'''
	LeetCode Problem 9. Palindrome Number
	Determine whether an integer is a palindrome without allocating extra space
	'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
            return False
            
        reverse=0
        
        while(x>reverse):
            reverse = reverse*10 + x%10
            x = x/10
        
        return reverse==x or x == reverse/10