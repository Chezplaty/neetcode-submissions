class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.makeTrie(words)
        res = []
        visited = set()

        def dfs(row: int, col: int, cur: TrieNode):
            char = board[row][col]

            if (row, col) in visited:
                return
            
            if char not in cur.children:
                return

            save_cur = cur
            cur = cur.children[char]
            visited.add((row, col))

            if cur.word:
                res.append(cur.word)
                cur.word = None #prevent word from being found again
            
            #go left
            if (col - 1) >= 0:
                dfs(row, col - 1, cur)

            #go up
            if (row - 1) >= 0:
                dfs(row - 1, col, cur)
            
            #go right
            if (col + 1) < len(board[0]):
                dfs(row, col + 1, cur)
            
            #go down
            if (row + 1) < len(board):
                dfs(row + 1, col, cur)
            
            visited.remove((row, col))
            cur = save_cur
        
    #search for starting point
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        
        return res
    
    def makeTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word #indicates end of word
        
        return root
            



        