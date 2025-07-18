class Solution:
    def nextPermutation(self, nums):
        el_index = 0
        # searching for first decreasing element
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                el_index = i
                break
        
        if el_index==0:
            return nums.reverse()

        # searching for the smallest element greater than the first decreasing element in the subarray to the right of the first decreasing element
        small = el_index
        for i in range(el_index+1, len(nums)):
            if nums[i]>nums[el_index-1] and nums[i]<nums[small]:
                small = i
        
        # swapping first decreasing element and the small found
        nums[small], nums[el_index-1] = nums[el_index-1], nums[small]

        #reversing the subarray to find the final permutation required
        nums[el_index:-1].reverse()

        return nums
    
if __name__=="__main__":
    obj = Solution()
    arr = list(map(int, input("Enter an array of integers: ").split()))
    res = obj.nextPermutation(arr)
    print("Next Permutation: ", res)