from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        ind=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            ind[a]+=1
        q=deque([i for i in range(numCourses) if ind[i]==0])

        completed=0
        
        while q:
            node=q.popleft()
            completed+=1

            for nei in graph[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        return completed==numCourses