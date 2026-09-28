class DSU:
    def __init__(self,n):
        self.parent=[a for a in range(n)]
        self.size=[1]*(n)
        self.component=n


    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]  

    def union(self,a,b):
        pa=self.find(a)
        pb=self.find(b)
        if pa==pb:
            return False

        self.component-=1
        if self.size[pa]>=self.size[pb]:
            self.size[pa]+=self.size[pb]
            self.parent[pb]=pa
        else:
            self.size[pb]+=self.size[pa]
            self.parent[pa]=pb
        return True



    def numComponents(self): 
        return self.component


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        s=len(isConnected)
        dsu=DSU(s)
        for i in range(s):
            for j in range(s):
                if isConnected[i][j]==1:
                    dsu.union(i,j)

        return dsu.numComponents()    
