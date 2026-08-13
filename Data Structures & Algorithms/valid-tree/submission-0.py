from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        edgeMap = defaultdict(list)
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        visited = set()
        def dfs(node: int, prev: int):

            if node in visited:
                return False
            
            visited.add(node)
            for edge in edgeMap[node]:
                if edge == prev:
                    continue
                if not dfs(edge, node): #propagate false
                    return False
            
            return True

        if not dfs(0, None):
            return False
            
        return len(visited) == n

