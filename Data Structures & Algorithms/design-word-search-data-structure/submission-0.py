class TrieNode:

    def __init__(self):
        self.children = {} # {'c': TrieNode()}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        i = 0

        def dfs(cur: TrieNode, i: int):
            while i < len(word):
                char = word[i]
                if char == '.':
                    for node in cur.children.values():
                        cur = node
                        if dfs(cur, i + 1):
                            return True

                    #went through all paths, did not find any
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
                
                i += 1
            
            return cur.endOfWord

        return dfs(cur, i)



