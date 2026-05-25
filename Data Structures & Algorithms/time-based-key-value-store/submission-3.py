class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        to_be_set = [timestamp, value]
        if self.storage.get(key):
            self.storage[key].append(to_be_set)
        else:
            self.storage[key] = [to_be_set]

    def search(self, container: list[list[int, str]], target) -> str:
        left, right = 0, len(container) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if container[mid][0] <= target:
                result = container[mid][1]
                left = mid + 1                
            else:
                right = mid - 1
        return result

    def get(self, key: str, timestamp: int) -> str:
        if self.storage.get(key):
            list_of_values = self.storage[key]
            result = self.search(list_of_values, timestamp)
            return result
        else:
            return ""
