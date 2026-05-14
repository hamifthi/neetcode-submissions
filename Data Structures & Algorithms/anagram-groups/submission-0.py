class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_sorted_strs = []
        for string in strs:
            chars = list(string)
            chars.sort()
            list_of_sorted_strs.append("".join(chars))
        groups = {}
        for i in range(len(list_of_sorted_strs)):
            if list_of_sorted_strs[i] in groups:
                groups[list_of_sorted_strs[i]].append(i)
            else:
                groups[list_of_sorted_strs[i]] = [i]
        result = []
        for _, v in groups.items():
            group = []
            for i in v:
                group.append(strs[i])
            result.append(group)
        return result