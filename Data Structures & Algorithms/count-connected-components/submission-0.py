class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self,n):
                self.parent=[x for x in range(n)]
                self.size=[1]*n
                self.num_components=n
            
            def find(self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                rootX,rootY=self.find(x),self.find(y)
                if rootX!=rootY:
                    if self.size[rootX]<self.size[rootY]:
                        self.parent[rootX]=rootY
                        self.size[rootY]+=self.size[rootX]
                    else:
                        self.parent[rootY]=rootX
                        self.size[rootX]+=self.size[rootY]
                    self.num_components-=1
                    return True
                return False

            def NumComponents(self):
                return self.num_components


        connected=UnionFind(n)
        for u,v in edges:
            connected.union(u,v)
        return connected.NumComponents()