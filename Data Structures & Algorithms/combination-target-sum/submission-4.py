class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        
        def dfs(idx, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(idx, len(nums)):
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()
        
        dfs(0, target)
        return result