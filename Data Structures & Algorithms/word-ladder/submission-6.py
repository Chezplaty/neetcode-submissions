from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordMap = defaultdict(list)

        #build adjacency list
        for word in wordList:
            for i in range(len(word)):
                parent = word[:i] + '*' + word[i+1:] 
                wordMap[parent].append(word)
        
        #BFS with beginWord, replace the first letter
        q = deque()
        visited = set()
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    parent = word[:i] + '*' + word[i+1:] 
                    for w in wordMap[parent]:
                        if w == endWord:
                            return res + 1 # add one for final word
                        if w not in visited:
                            q.append(w)
                            visited.add(w)
            res += 1
        
        return 0 
        


    