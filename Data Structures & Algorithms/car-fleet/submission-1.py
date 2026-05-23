class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([[position[i], speed[i]] for i in range(len(position))], reverse=True)
        stack = []
        print(pairs)
        for i in range(len(pairs)):
            time = (target - pairs[i][0]) / pairs[i][1]
            # print(time)
            if len(stack) == 0:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    pass
                else:
                    stack.append(time)
        return len(stack)