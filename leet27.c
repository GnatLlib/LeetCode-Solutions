/**

	LeetCode Question 27.
	Remove Element
	
	Given an array and a value, remove all instances of that value in place and 
	return the new length
	
	**/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        for(int i = 0; i<nums.size();i++)
        {
            
            if (nums[i]==val)
            {
                nums.erase(nums.begin()+i);
                i--;
            }
        }
        return nums.size();
        
    }
};