class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n=len(matrix)
        for x in range(n):
            for j in range(x+1,n):
                matrix[x][j],matrix[j][x]=matrix[j][x],matrix[x][j]

        