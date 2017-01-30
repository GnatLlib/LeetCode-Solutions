"""
	LeetCode Problem 70. Climbing Stairs
	Solved using Dynamic Programming
	"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n ==2:
            return 2
        result = [0 for i in range(n+1)]
        result[1] = 1
        result[2] = 2
        
        for i in range(3,n+1):
            result[i] = result[i-2] + result[i-1]
            
        return result[n]