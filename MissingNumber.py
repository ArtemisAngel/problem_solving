# T(O) = N

class Solution:
    def missingNumber(self, nums):
        n = len(nums)+1
        sum1 = (n*(n+1))//2 
        sum2 = sum(nums) #O(n)
        return sum1-sum2

if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split(" ")))
    res = obj.missingNumber(arr)
    print(res)