class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row, col = 0, 0
        visited = set()
        
        #i - index of letter to search for
        def backtrack(i, row, col):
            
            if i == len(word):
                return True

            #out of bounds
            if not(0 <= row < len(board)) or not(0 <= col < len(board[0])):
                return False
                
            #not a letter in the word
            if board[row][col] != word[i]:
                return False

            #already visited
            if (row, col) in visited:
                return False

            #search next letter
            i += 1
            visited.add((row,col))

            #search all four
            res = (backtrack(i, row - 1, col) or backtrack(i, row, col + 1)
                    or backtrack(i, row + 1, col) or backtrack(i, row, col - 1))
            
            if res:
                return True

            visited.remove((row,col))
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if len(word) == 1:
                        return True
                    
                    #start searching
                    if backtrack(0, r, c):
                        return True
  
        #no matches
        return False


        






        