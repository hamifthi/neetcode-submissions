class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            left, right = 0, len(line) - 1
            if target >= line[left] or target <= line[right]:
                while left <= right:
                    mid = (left + right) // 2
                    if line[mid] == target:
                        return True
                    elif line[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False