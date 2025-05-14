class Solution:
    def moveZeroes(self, nums):
        ind = 0
        for i in nums:
            if i!=0:
                nums[ind] = i
                ind+=1
        while ind<len(nums):
            nums[ind] = 0
            ind+=1
        return nums

if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split(" ")))
    res = obj.moveZeroes(arr)
    print(res)