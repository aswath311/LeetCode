from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        valueCount = {}
        tripletSet = set()
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         thirdVal = 0 - (nums[i]+nums[j])
        #         if thirdVal in nums[j+1:]:
        #             pairString = str(sorted([nums[i], nums[j], thirdVal]))
        #             if pairString not in pairs:
        #                 pairs.add(pairString)
        #                 result.append([nums[i], nums[j], thirdVal]) 
        for i in nums:
            valueCount[i] = valueCount.get(i, 0) + 1
        values = list(valueCount.keys())
        for i in range(len(values)-1):
            for j in range(i+1, len(values)):
                thirdValue = 0 - (values[i] + values[j])
                if thirdValue in valueCount:
                    if (thirdValue == values[i] and valueCount[thirdValue]<2) or (thirdValue == values[j] and valueCount[thirdValue]<2):
                        continue
                    tripletString = str(sorted([values[i], values[j], thirdValue]))
                    if tripletString not in tripletSet:
                        tripletSet.add(tripletString)
                        result.append([values[i], values[j], thirdValue])
        if valueCount.get(0, 0) > 2:
            result.append([0,0,0])
            
        return result

s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))
# print(s.threeSum([0,1,1]))
# print(s.threeSum([0,0,0]))
# print(s.threeSum([1,1,-2]))
print(s.threeSum([1,2,-2,-1]))