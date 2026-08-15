class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find, if we see that two nodes already have the same parent
        #cycle, that edge is the one to be removed

        par = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(node):

            if par[node] != node:
                par[node] = find(par[node])
            
            return par[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2: #cycle detected
                return True
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
            
            return False #no cycle
        
        for a, b in edges:
            if union(a, b):
                return [a, b]
        
        return []