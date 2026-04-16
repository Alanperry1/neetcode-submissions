class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        new=[]
        for i in range(n+1):
            result.append(bin(i)[2:])
        for i in result:
            new.append(i.count("1"))
        return new