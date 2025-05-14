# T(O) = N

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[k]:
                k+=1
                nums[k] = nums[i]

        return k+1

if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Value: ").split(" ")))
    res = obj.removeDuplicates(arr)
    print(res)