class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        result=[[0]*rows for i in range(cols)]
        for x in range(rows):
            for j in range(cols):
                result[j][x]=matrix[x][j]

        return result