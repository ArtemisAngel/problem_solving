
# Pascal's Triangle

class Solution():
    def PascalTriangle(self, numRows):
        pas = [[1]]

        for i in range(numRows-1):
            row = []
            temp = [0] + pas[-1] + [0]
            
            for j in range(len(pas[-1])+1):
                row.append(temp[j]+temp[j+1])
            
            pas.append(row)

        return pas
    
if __name__=="__main__":
    obj = Solution()
    numRows = int(input("Enter number of rows for Pasacal's Triangle: "))
    res = obj.PascalTriangle(numRows)
    print(res)

# T(O) = n^2