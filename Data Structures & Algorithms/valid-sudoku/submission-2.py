from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        length = len(board)
        square_map = defaultdict(set)
        column_map = defaultdict(set)
        row_map = defaultdict(set)

        for r in range(length):
            for c in range(length):

                num = board[r][c]
                if num == '.':
                    continue
    
                if num in row_map[r] or num in column_map[c]\
                    or num in square_map[(r//3,c//3)]:
                    return False
                
                row_map[r].add(num)
                column_map[c].add(num)
                square_map[(r//3,c//3)].add(num)
        
        return True
