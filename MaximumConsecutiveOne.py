class Solution:
    def findMaxConsecutiveOnes(self, nums):
        rec = 0
        count = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                count = 0
            if count>rec:
                rec = count
        return rec
if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split(" ")))
    res = obj.findMaxConsecutiveOnes(arr)
    print(res)
    