class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {i: 0 for i in nums}
        for i in range(len(nums)):
            counter[nums[i]] += 1
        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        result = []
        keys = [i for i in sorted_counter.keys()]
        for i in range(k):
            result.append(keys[i])
        return result