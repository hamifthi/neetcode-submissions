class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temps[i] > temps[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        
        return result