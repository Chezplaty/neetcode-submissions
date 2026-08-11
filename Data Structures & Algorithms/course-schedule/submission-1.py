from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)


        visiting = set()

        def dfs(course_a):
            
            if not prereqs[course_a]: # no prereqs, can be completed
                return True

            if course_a in visiting: #we have already been here, there is a cycle
                return False

            prereq_list = prereqs[course_a]
            visiting.add(course_a)

            for prereq in prereq_list:
                if not dfs(prereq): #prereq not cleared, propagate up
                    return False
            
            visiting.remove(course_a)
            prereqs[course_a] = []
            return True
            
        for a, b in prerequisites:
            if not dfs(a):
                return False

        return True
        
        