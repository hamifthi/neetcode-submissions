class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(indexes: List[int], subset: List[int]):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):
                if i in indexes:
                    continue
                indexes.append(i)
                subset.append(nums[i])
                dfs(indexes, subset)
                indexes.pop()
                subset.pop()
        
        dfs([], [])
        return result