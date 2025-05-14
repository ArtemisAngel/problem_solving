class Solution:
    def singleNumber(self, nums):
        #your code goes here
        seen = set()
        dup = set()
        for i in nums:
            if i in seen:
                dup.add(i)  #visited once
            else:
                seen.add(i) #not visited even once
        for i in seen:
            if i not in dup:
                return i
            
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Space Separated Values: ").split()))
    res = obj.singleNumber(arr)
    print(res)