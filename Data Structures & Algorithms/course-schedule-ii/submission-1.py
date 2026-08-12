from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        in_edges = [0] * numCourses
        preMap = defaultdict(list)

        for prereq in prerequisites: #map edges and course prereqs
            a, b = prereq
            preMap[a].append(b)
            in_edges[b] += 1
        
        q = deque()
        for i in range(numCourses):
            if in_edges[i] == 0: #starting point
                q.append(i)
        
        visited = 0
        while q:
            course = q.popleft()
            visited += 1
            res.insert(0, course)
            #delete the edge course pointed to
            for node in preMap[course]:
                in_edges[node] -= 1
                if in_edges[node] == 0: 
                    q.append(node)
        
        if visited == numCourses:
            return res
        
        return []

