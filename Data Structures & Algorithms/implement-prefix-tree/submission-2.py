#naive solution

class PrefixTree:

    def __init__(self):
        self.words = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        self.prev = word


    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if word[:len(prefix)] == prefix:
                return True

        return False
        
        