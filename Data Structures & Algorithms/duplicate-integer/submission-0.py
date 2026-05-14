class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {i:0 for i in nums}
        for i in nums:
            result[i] += 1
        for v in result.values():
            if v > 1:
                return True
        return False