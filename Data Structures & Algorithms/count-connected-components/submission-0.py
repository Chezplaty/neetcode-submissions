from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        visited = set()
        res = 0

        def dfs(node):

            if node in visited:
                return
            
            visited.add(node)
            for adj_node in edgeMap[node]:
                dfs(adj_node)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res