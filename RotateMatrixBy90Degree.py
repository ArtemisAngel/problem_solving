

class Solution():
    def RotateMatrix(self, mat, n):

        #Transposing the Matrix
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        #Reversing the Transposed Matrix
        for i in range(n):
            mat[i].reverse()

        return mat
    
if __name__ == "__main__":
    obj = Solution()
    matrix = []
    n = int(input("Enter number of rows in the matrix: "))
    for i in range(n):
        row = list(map(int, input("Enter values for the row: ").split()))
        matrix.append(row)

    print("Inputted Matrix: ", matrix)

    result = obj.RotateMatrix(matrix, n)

    print("Rotated Matrix: ", result)