class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]
        seen_diff = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen_diff.keys():
                return [seen_diff[difference], i]
            else:
                seen_diff[nums[i]] = i
