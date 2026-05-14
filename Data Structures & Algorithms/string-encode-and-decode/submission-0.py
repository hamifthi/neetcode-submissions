class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string + "€"
        return result
    def decode(self, s: str) -> List[str]:
        strings = []
        result = ""
        for character in s:
            if ord(character) < 127:
                result += character
            elif ord(character) == 8364:
                strings.append(result)
                result = ""
        return strings