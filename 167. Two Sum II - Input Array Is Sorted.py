from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(numbers)):
            if numbers[i] not in map:
                map[numbers[i]] = i
        for i in numbers:
            j = target - i
            if i == j and numbers[map[i]+1] == i:
                return [map[i]+1, map[i]+2]
            if j in map:
                return [map[i]+1, map[j]+1]
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,-1,-1,0], -1))
print(s.twoSum([0,0,3,4], 0))