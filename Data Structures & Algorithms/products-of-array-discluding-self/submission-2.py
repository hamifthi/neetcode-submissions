class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        has_zero = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                has_zero += 1
        result = []
        for i in range(len(nums)):
            if nums[i] != 0 and has_zero == 0:
                result.append(product//nums[i])
            elif nums[i] != 0 and has_zero == 1:
                result.append(0)
            elif nums[i] != 0 and has_zero > 1:
                result.append(0)
            elif nums[i] == 0 and has_zero == 1:
                result.append(product)
            elif nums[i] == 0 and has_zero > 1:
                result.append(product*nums[i]) 
        return result