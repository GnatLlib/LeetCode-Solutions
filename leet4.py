"""
	LeetCode 4. Median of two sorted arrays
	
	Given two sorted arrays, return the median.
	"""
	The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        
        while(len(nums1)+len(nums2)>2):
            
            if (nums1 and nums2):
                if (nums1[0]<nums2[0]):
                    nums1.pop(0)
                else:
                    nums2.pop(0)
            
                if(nums1 and nums2):
                    if (nums1[-1]>nums2[-1]):
                        nums1.pop()
                    else:
                        nums2.pop()
                elif(nums1):
                    nums1.pop()
                else:
                    nums2.pop()
            
            elif nums1:
                nums1.pop(0)
                nums1.pop()
                
            else:
                nums2.pop(0)
                nums2.pop()
                
        if nums1:
            if nums2:
                return ((float(nums1[0])+nums2[0])/2)
            elif (len(nums1)>1):
                return ((float(nums1[0])+nums1[1])/2)
            else:
                return nums1[0]
            
        if nums2:
            if len(nums2)>1:
                return ((float(nums2[0])+nums2[1])/2)
            else:
                return nums2[0]
                
        
            
            
            
            
            
        
        