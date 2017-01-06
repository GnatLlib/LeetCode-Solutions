'''
	LeetCode Problem 6. ZigZag Conversion

	'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        result=['' for x in range(numRows)]
        string=''
        
        counter=0
        dir = True
        for i in range(len(s)):
            result[counter] = result[counter] + s[i]
            
            if dir == True:
                counter = counter+1
            if dir == False:
                counter = counter-1
            if counter>numRows-1:
                dir = False
                counter=counter-2
            if counter<0:
                dir = True
                counter=counter+2
        for i in result:
            string = string+i
        return string
                