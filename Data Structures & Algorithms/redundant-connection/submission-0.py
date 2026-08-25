class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self,n):
                self.parent=[x for x in range(n)]
                self.size=[1]*n

            def find(self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])

                return self.parent[x]


            def union(self,x,y):
                rootX,rootY=self.find(x),self.find(y)
                if rootX!=rootY:
                    if self.size[rootX]<self.size[rootY]:
                        self.parent[rootX]=self.parent[rootY]
                        self.size[rootY]+=self.size[rootX]

                    else:
                        self.parent[rootY]=self.parent[rootX]
                        self.size[rootX]+=self.size[rootY]
                    return True

                return False

        n=len(edges)+1
        connections=UnionFind(n)
        for u,v in edges:
            if not connections.union(u,v):
                return [u,v]