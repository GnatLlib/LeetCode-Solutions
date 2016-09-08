/** 
	LeetCode Question 283.
	Move Zeroes
	
	Given an array nums, write a function to move all the 0's to the end of it
	while maintaining the relative order of the non-zero elements
	

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int k = nums.size();
        for(int i = 0; i<k; i++)
        {
            if(nums[i]==0)
            {
                nums.erase(nums.begin()+i);
                i--;
                k--;
                nums.push_back(0);
            }
            
        }
        
    }
};