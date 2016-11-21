"""
	LeetCode Problem 53. Maximum Subarray
	Find the contiguous subarray within an array
	
	Solved using Kadane's algorithm
	"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax=nums[0]
        globMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax+nums[i])
            globMax = max(currMax, globMax)
        
        return globMax