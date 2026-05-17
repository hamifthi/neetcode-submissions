import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = {str(i): i for i in range(-200, 201)}
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []
        if len(tokens) == 1:
            if numbers.get(tokens[0]):
                return int(tokens[0])
            else:
                return 0
        if len(tokens) == 2:
            try:
                result = ops[tokens[1]](tokens[0], 0)
            except ZeroDivisionError:
                return 0
        for token in tokens:
            if numbers.get(token) is not None:
                stack.append(numbers[token])
            else:
                j = stack.pop()
                i = stack.pop()
                try:
                    result = int(ops[token](i, j))
                except ZeroDivisionError:
                    continue
                stack.append(result)
        return stack.pop()