class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_a = [i for i in s]
        chars_b = [j for j in t]
        chars_a.sort()
        chars_b.sort()
        if chars_a == chars_b:
            return True
        return False