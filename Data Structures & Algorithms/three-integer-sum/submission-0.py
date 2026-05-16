class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index in range(len(nums) - 2):
            i, j = index + 1, len(nums) - 1
            sum = nums[index] + nums[i] + nums[j]
            while i < j:
                sum = nums[index] + nums[i] + nums[j]
                if sum == 0:
                    pair = [nums[index], nums[i], nums[j]]
                    result.append(pair) if pair not in result else None
                    i += 1
                    j -= 1
                if sum < 0:
                    i += 1
                if sum > 0:
                    j -= 1
        return result