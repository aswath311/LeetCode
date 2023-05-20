from typing import List
class Solution:
    def waterBetween(self, height, i, j):
        waterVol = min(height[i], height[j]) * (j-i-1)
        landCoveredVol = 0
        for h in height[i+1:j]:
            landCoveredVol += h
        return waterVol - landCoveredVol

    def trappedWaterHighestPoint(self, height: List[int]):
        waterCollected = 0
        i=0
        j = 1
        while i < len(height) and j < len(height):
            if(height[j] >= height[i]):
                waterCollected += self.waterBetween(height, i, j)
                i = j
            j += 1
            # if j == len(height):
            #     i +=1
        # waterCollected += self.waterBetween(height, i, j-1)
        return waterCollected, j-i    

    def trap(self, height: List[int]) -> int:
        trappedWaterL, i =  self.trappedWaterHighestPoint(height) 
        trappedWaterR, j = self.trappedWaterHighestPoint(height[::-1][:i])
        return trappedWaterL + trappedWaterR
        
        
        # #brute force
        # waterCollected = 0
        # # for i in range(max(height)):
        # maxHeight = max(height)
        # i = 1
        # while i <= maxHeight:
        #     left = right = 0
        #     waterCoverInLevel = 0
        #     j = 0
        #     # for j in range(len(height)):
        #     while j < len(height):
        #         if  height[j] >= i:
        #             left = j
        #             k = j+1
        #             # for k in range(j+1, len(height)):
        #             while k < len(height):
        #                 if height[k] >= i:
        #                     right = k
        #                     waterCoverInLevel += right - left - 1
        #                     left = right
        #                     k = right = right + 1
        #                     j = left
        #                 else:
        #                     k += 1
        #         j +=1
        #     i += 1
        #     waterCollected += waterCoverInLevel
        # return waterCollected

s = Solution()

print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
print(s.trap([2,0,2]))
print(s.trap([4,2,3]))

print(s.trap([10,0,0,0,0,8]))