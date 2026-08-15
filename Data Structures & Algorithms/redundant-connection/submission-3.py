from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edgeMap = defaultdict(list)

        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        cycle = {} #use dic instead of set to preserver insertion order
        def dfs(node, parent):

            if node in cycle:
                for n in list(cycle.keys()): #create a list/copy because cycle changes throughout loop
                    if n == node: #Found the cycle
                        return True
                    del cycle[n] #Remove everything not in the cycle

            cycle[node] = None
            for adj_node in edgeMap[node]:
                if adj_node != parent and dfs(adj_node, node):
                    return True
            
            del cycle[node]
            return False

        dfs(edges[0][0], -1) #start at first node in list, no parent
        for i in range(len(edges) -1, -1, -1):
            a, b = edges[i]
            if a in cycle and b in cycle: 
                return [a, b]
        
        return []