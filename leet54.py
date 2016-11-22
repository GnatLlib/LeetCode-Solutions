"""
	LeetCode Problem 54. Spiral Matrix
	Given a matrix of m x n elements, return all elements in spiral order
	"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        """
        if len(matrix)<1:
            return matrix
        result=[]
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        
        while(left <= right and top<= bottom):
            for i in range(left, right+1):
                if top<=bottom:
                    result.append(matrix[top][i])
        
            top = top + 1
        
            for i in range(top, bottom+1):
                if left<=right:
                    result.append(matrix[i][right])
        
            right = right-1
        
            for i in range(right, left-1, -1):
                if top<=bottom:
                    result.append(matrix[bottom][i])
        
            bottom = bottom-1
            
            for i in range(bottom, top-1, -1):
                if left<=right:
                    result.append(matrix[i][left])
            left = left + 1
        
        return result