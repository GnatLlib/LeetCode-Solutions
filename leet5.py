"""
	Leetcode Problem 5. Longest Palindromic Substring
	"""
class Solution(object):
    maxlen = 1
    start = 0
    def extend(self,s,i,k):
        while(i>=0 and k < len(s) and s[i] == s[k]):
            i = i-1
            k = k+1
        if(self.maxlen < k-i-1):
            self.start = i+1
            self.maxlen = k-i-1
            
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
            
        for i in range(len(s)-1):
            self.extend(s,i,i)
            self.extend(s,i,i+1)
        
        
        return s[self.start: self.start + self.maxlen]