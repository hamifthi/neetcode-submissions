class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s2) == 1 and s1 == s2:
            return True
        state = {}
        for i in s1:
            state[i] = state.get(i, 0) + 1
        l = 0
        for i in range(len(s2)):
            if state.get(s2[i]):
                l, r = i, i
                while r - l != len(s1):
                    r += 1
                if "".join(sorted(s2[l: r])) == "".join(sorted(s1)):
                    return True
        return False
