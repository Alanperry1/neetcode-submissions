class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n
        for col in range(m-1):
            newRow=[1]*n
            for r in range(n-2,-1,-1):
                newRow[r]=newRow[r+1]+row[r]
            row=newRow
        return row[0]