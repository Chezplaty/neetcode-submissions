class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjMap = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjMap[w1[j]].add(w2[j])
                    break

        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in adjMap[c]:
                if dfs(nei): #True means cycle detected
                    return True
                
            res.append(c)

            visit[c] = False
            return False
        
        for c in adjMap:
            if c not in visit:
                if dfs(c):
                    return ""
        
        return "".join(res[::-1])

