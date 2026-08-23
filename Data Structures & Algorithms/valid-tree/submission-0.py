from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visit=set()
        def dfs(node,prev):
            if node in visit:
                return False
            visit.add(node)

            for nei in graph[node]:
                if nei==prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n