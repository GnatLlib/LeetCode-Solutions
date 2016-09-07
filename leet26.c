/**
	LeetCode question 26.
	Remove duplicates from sorted array
	
	Given a sorted array, remove the duplicates in place such that each element
	appear only once and return the new length.
	
	**/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
       if(nums.size()==0)
       {
           return 0;
       }
       
        for(int i = 0; i<nums.size()-1; i++)
        {
            
            if(nums[i] ==nums[i+1])
            {
                nums.erase(nums.begin()+i+1);
                i--;
            }
        }
        
        return nums.size();
    }
};