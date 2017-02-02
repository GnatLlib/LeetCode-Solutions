"""
	LeetCode Problem 60. Permutation Sequence
	Return the kth permutation of a set of length n 
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        result = ''
        factorial = [1 for _ in range(n+1)]
        for i in range(1,n+1):
            factorial[i] = i * factorial[i-1]
        
        numbers = [x for x in range(1,n+1)]
      
        k = k-1
        for i in range(1,n+1):
            index = k/factorial[n-i]
            
            result = result + str((numbers[index]))
            numbers.pop(index)
            k -= index*factorial[n-i]
        
        return result