'''
	LeetCode 62. Unique paths
	
	A robot is located in top-left corner of m x n grid. How many unique paths are there to 
	opposite corner?
		'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n ==1:
            return 1
        m = m-1
        n = n-1
        
        return (math.factorial(m+n)/(math.factorial(m) * math.factorial(n)))