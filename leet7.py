'''
	LeetCode Problem 7. Reverse Integer
	Reverse digits of an integer. In case of overflow for a 32-bit integer, return 0
	'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse=0
        neg = False
        if x < 0:
            neg = True
            x = -x
        
        
        
        while x!=0:
            reverse = 10*reverse + x%10
            x = x/10
        if neg:
            reverse= -reverse
            
        if reverse < -2147483648 or reverse> 2147483647:
            return 0
        return reverse