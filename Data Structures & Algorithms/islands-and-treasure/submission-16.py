from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs on treasure chest
        rows, columns = len(grid), len(grid[0])

        def bfs(queue, visited):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            distance = 0

            while queue:
                distance += 1
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        r, c = row + dr, col + dc
    
                        if 0 <= r < rows and 0 <= c < columns and (r, c) not in visited and grid[r][c] != -1 and grid[r][c] != 0:
                            if grid[r][c] == 2147483647 or grid[r][c] > distance:
                                grid[r][c] = distance
                            visited.add((r, c))
                            queue.append((r, c))
            return


        visited = set()
        queue = deque([])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        bfs(queue, visited)
        
        return