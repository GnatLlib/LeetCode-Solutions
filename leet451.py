"""
	Leetcode problem 451 Sort Character By Frequency
	
	Given a string, sort it in decreasing order based on frequency of characters
	
	Ex:
	Input: tree
	Ouput: eert
	
	"""
	
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = list(s)
        char = []
        map = []
        for i in str:
            if i not in char:
                char.append(i)
                map.append((i, int(str.count(i))))
        map.sort(key = lambda x: x[1], reverse=True)
       
        result= ''
        for (x,y) in map:
            result = result + x*y
        
        return result