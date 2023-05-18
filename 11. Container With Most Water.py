from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxVol = 0
        while i<j:
            volUnder = (j-i) * min(height[i], height[j])
            if(volUnder > maxVol):
                maxVol = volUnder
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return maxVol

        ## brute force
        # maxArea = 0
        # leftMax = height[0]
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         waterArea = (j-i) * min(height[i], height[j])
        #         if(waterArea > maxArea):
        #             maxArea = waterArea
        # return maxArea
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))