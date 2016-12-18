"""
	LeetCode Problem 3. Longest substring without repeating characters
	Solved using dynamic programming
	"""
class Solution(object):
    
    def isUnique(self,s):
        return len(set(s))==len(s)
        
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        
        maxlen = 1
        start = 0
        
        for i in range(len(s)):
            if i-maxlen >= 0 and self.isUnique(s[i-maxlen:i+1]):
                maxlen = maxlen + 1
                
         
        return maxlen