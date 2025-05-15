class Solution:
    def searchMatrix(self, n, m, mat, target):
        low = 0
        high = n*m-1
        while low<=high:
            mid = (low+high)//2
            row = mid//m
            col = mid%m
            if mat[row][col]==target:
                return "True"
            elif target<mat[row][col]:
                high = mid-1
            else:
                low = mid+1
        return "False"


if __name__=="__main__":
    obj = Solution()
    arr = []
    n = int(input("Enter number of rows in matrix: "))
    m = int(input("Enter number of columns in matrix: "))
    arr = []
    for i in range(n):
        val = list(map(int, input("Space Separated Values: ").split(" ")))
        arr.append(val)
    print("Input Matrix: ", arr)
    tar = int(input("Enter Target to search: "))
    res = obj.searchMatrix(n, m, arr, tar)
    print(res)