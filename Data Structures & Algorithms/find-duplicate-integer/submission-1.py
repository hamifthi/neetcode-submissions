class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        dup = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                dup = nums[i]
        return dup