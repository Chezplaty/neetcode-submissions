class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        res = n
        
        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
                
            return par[node]

        def union(n1, n2): #combine two edges
            p1, p2 = find(n1), find(n2)

            if p1 == p2: #same parents, already connected
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for a, b in edges:
            res -= union(a, b)
        
        return res

