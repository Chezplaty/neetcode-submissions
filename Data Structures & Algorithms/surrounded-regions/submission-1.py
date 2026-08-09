class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #start at any O in the border, if it can reach others Os, those cannot be captured, everything else is
        #if it hits any Os, mark them as visited
        #then go through the whole grid, any O not visited will be captured
        row_len = len(board)
        col_len = len(board[0])
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if (r < 0 or r >= row_len or c < 0 or c >= col_len
                or (r, c) in visited or board[r][c] == 'X'):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        #check borders for )
        for c in range(col_len):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[row_len - 1][c] == 'O':
                dfs(row_len - 1, c)
        
        for r in range(row_len):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][col_len - 1] == 'O':
                dfs(r, col_len - 1) 
        
        for r in range(row_len):
            for c in range(col_len):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

        
