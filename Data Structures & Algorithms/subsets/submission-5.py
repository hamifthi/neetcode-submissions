class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(subset, idx):
            if idx == len(nums):
                result.append(subset[:])
                return
            
            backtrack(subset, idx + 1)
            subset.append(nums[idx])
            backtrack(subset, idx + 1)
            subset.pop()

        backtrack([], 0)
        return result
        