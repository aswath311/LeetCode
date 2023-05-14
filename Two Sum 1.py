class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return []
    
s = Solution()
print(s.twoSum([3,2,4], 6))