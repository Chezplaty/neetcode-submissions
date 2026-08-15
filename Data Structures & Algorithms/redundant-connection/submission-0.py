from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        edgeMap = defaultdict(list)
        visited = set() # check if neighbor is already visited
        
        def dfs(node, target):
            if node == target:
                return True

            visited.add(node)

            for adj_node in edgeMap[node]:
                if adj_node not in visited:
                    if dfs(adj_node, target):
                        return True
            
            visited.remove(node)
            return False

        
        for a, b in edges:
            if dfs(a, b): # cycle is found
                return [a, b]
            
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        return []
        
