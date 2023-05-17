from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for i in nums:
            if i-1 not in numSet:
                length = 1
                while (i + length) in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
    
s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0]))
                
