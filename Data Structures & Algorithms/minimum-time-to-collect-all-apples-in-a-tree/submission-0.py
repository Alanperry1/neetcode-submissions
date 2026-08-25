class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(curr,prev):
            time=0
            for nei in adj[curr]:
                if nei==prev:
                    continue
                childTime=dfs(nei,curr)
                if hasApple[nei] or childTime>0:
                    time+=childTime+2

            return time

        return dfs(0,-1)