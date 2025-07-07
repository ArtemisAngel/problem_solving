# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution():
    def MajorityElement(self, nums):
        freq = {}
        n = len(nums)

        # maintaining a frequency array
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]]+=1

        # returning key with occurence greater than n/2
        for i in freq:
            if freq[i]>int(n/2):
                return i
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Enter an array of integers: ").split()))
    res = obj.MajorityElement(arr)
    print(res)