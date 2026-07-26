class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs_helper(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return

            if (r, c) in visited:
                return

            if grid[r][c] == "0":
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs_helper(r + dr, c + dc)
            return

        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs_helper(i, j)
                    number_of_islands += 1
        
        return number_of_islands