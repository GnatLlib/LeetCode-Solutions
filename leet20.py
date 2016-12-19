"""
	LeetCode Problem 20. Valid Parentheses
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
	"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = ['(','{','[']
        end = [')','}',']']
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in start:
                stack.append(s[i])
            if s[i] in end:
                if not stack or start.index(stack.pop()) != end.index(s[i]):
                    return False
        if stack:
            return False
        return True