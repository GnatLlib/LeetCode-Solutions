'''
	LeetCode Problem 58. Find length of last word in string
	'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        wordstarted = False
        if len(s)==0:
            return 0
        
        
        for i in s[::-1]:
            if not wordstarted:
                if i!=' ':
                    wordstarted = True
                    
            if wordstarted:
                
                if i ==' ':
                    return count
                else:
                    count = count+1
        
        return count