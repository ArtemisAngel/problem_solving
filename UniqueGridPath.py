# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

class Solution():
    def RoboPath(self, m, n):
        N = m+n-2   # total steps the robot takes for a particular grid
        R = m-1     # maximum down steps the robot can take
        path = 1    # variable initialisation of total possible paths for robot

        # calculation using combination nCr = (N)C(R)
        for i in range(1, R+1):     # for getting the factorial
            path*=(N-R+i)/i

        return round(path)
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Enter the dimensions of the grid separated by space: ").split()))
    res = obj.RoboPath(arr[0], arr[1])
    print("Total Possible Pathways = ", res)