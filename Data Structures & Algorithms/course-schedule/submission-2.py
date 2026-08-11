from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [0] * numCourses
        preMap = defaultdict(list)
        for a, b in prerequisites:
            preMap[a].append(b)
            edges[b] += 1 #a points to b
        
        q = deque()
        visited = 0
        for i in range(len(edges)): #append all nodes with no in edges
            if edges[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop()
            visited += 1
            for prereq in preMap[course]:
                edges[prereq] -= 1
                if edges[prereq] == 0:
                    q.append(prereq)
        
        return visited == numCourses
