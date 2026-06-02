class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        states = {}
        longest = 0
        for end in range(len(s)):
            char = s[end]
            if states.get(char):
                states[char] += 1
            else:
                states[char] = 1
            while states.get(char) > 1:
                states[s[start]] -= 1
                if states.get(s[start]) == 0:
                    del states[s[start]]
                start += 1
            longest = max(end - start + 1, longest)
        return longest