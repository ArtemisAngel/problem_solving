class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        max = float('-inf')
        max2 = float('-inf')
        if len(nums)==1:
            return -1
        for i in range(n):
            if (nums[i]>max):
                max, max2 = nums[i], max
            elif (nums[i]>max2 and nums[i]!=max):
                max2 = nums[i]
        if max2==float('-inf'):
            max2=max
        return max2

if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input().split(" ")))
    print(obj.secondLargestElement(arr))