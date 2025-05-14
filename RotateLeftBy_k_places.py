# T(O) = N

class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)

        if k==0:
            return nums

        k%=n

        def Reverse(start, end):
            while(start<end):
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        
        Reverse(0, k-1)
        Reverse(k, n-1)
        Reverse(0, n-1)

        return nums
    
if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split(" ")))
    k = int(input("Rotation Value: "))
    res = obj.rotateArray(arr, k)
    print(res)