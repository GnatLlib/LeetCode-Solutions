"""
	LeetCode Problem 73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
	"""

class Solution(object):
    
    
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = False
        c = False
        
        if len(matrix) == 0:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range (0, rows):
            for j in range(0, cols):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if(i==0):
                        r = True
                    if(j==0):
                        c = True
        
        for i in range (1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0;
       
        for i in range (1, cols):
            if matrix[0][i] == 0:
                for j in range(1, rows):
                    matrix[j][i] = 0;
                    
        if r:
            for i in range(cols):
                matrix[0][i] = 0
        if c: 
            for i in range(rows):
                matrix[i][0] = 0