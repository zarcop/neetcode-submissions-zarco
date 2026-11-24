class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj_list = {i : [] for i in range(numCourses)}


        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visiting = set()
        visited = set()


        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
    
            visiting.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False


        return True


            
            

            




            

        