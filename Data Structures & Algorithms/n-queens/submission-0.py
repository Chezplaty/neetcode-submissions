class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res, subset = [], []
        occupied_cols = set()
        diag1 = set()
        diag2 = set()

        def is_occupied(row, col):
            #returns True if current row and col can be attacked
            
            if col in occupied_cols or row + col in diag1 or row - col in diag2:
                return True
            
            return False

        def backtrack(row):
            if row == n:
                res.append(subset[:])
                return

            cur_row = ['.' for _ in range(n)]

            for col in range(n):
                #skip if occupied column or diagonal
                if is_occupied(row, col):
                    continue

                # add queen to current row and column
                cur_row[col] = 'Q'
                occupied_cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                subset.append("".join(cur_row))

                backtrack(row+1)

                #remove queen
                subset.pop()
                occupied_cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
                cur_row[col] = '.'
        
        backtrack(0)
        return res
                
