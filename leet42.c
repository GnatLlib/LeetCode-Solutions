/**
	LeetCode #42.
	Trapping Rain Water
	
	Given n non-negative integers representing an elevation map where
	the width of each bar is 1, compute how much water it is able to trap after
	raining.
	
	**/

class Solution {
public:
    int trap(vector<int>& height) {
        
        int leftWall = 0;
        int rightWall = height.size()-1;
        
        int leftHeight = 0;
        int rightHeight = 0;
        
        int water = 0;
        
        while(leftWall<=rightWall)
        {
            if( height[leftWall] <= height[rightWall])
            {
                if(height[leftWall] > leftHeight)
                {
                    leftHeight = height[leftWall];
                    
                }
                else
                {
                    water += (leftHeight-height[leftWall]);
                }
                leftWall++;
            }
            else
            {
                if(height[rightWall] > rightHeight)
                {
                    rightHeight = height[rightWall];
                }
                else
                {
                    water += (rightHeight - height[rightWall]);
                }
                rightWall--;
            }
        }
        return water;
        
    }
};