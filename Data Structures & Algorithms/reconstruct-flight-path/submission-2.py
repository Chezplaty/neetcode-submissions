from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        edgeMap = defaultdict(list)

        #reverse ticket sort, to travel highest --> lowest then reverse later
        tickets.sort(reverse=True)
        for src, dest in tickets:
            edgeMap[src].append(dest)

        res = []
        def dfs(airport):
            
            while edgeMap[airport]:
                dfs(edgeMap[airport].pop()) #dfs until no edges, add dest   
            res.append(airport) # add backwards


        dfs("JFK")

        return res[::-1]