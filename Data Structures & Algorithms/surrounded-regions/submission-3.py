class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs_helper(r, c):
            if (r, c) in visited:
                return

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return

            if board[r][c] == "X":
                return

            visited.add((r, c))
            board[r][c] = "S"
            for dr, dc in directions:
                dfs_helper(r + dr, c + dc)
            return
        
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                dfs_helper(i, j)
        for j in [0, len(board[0]) - 1]:
            for i in range(len(board)):
                dfs_helper(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"

        return