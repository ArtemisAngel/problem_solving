# Given an integer array, find the subarray with the largest sum, and return its sum.

# solution through Kadane's Algorith

class Solution():
    def kadaneAlgo(self, arr):
        n = len(arr)
        sub_sum = arr[0]    # sum of selected subarray
        max_sum = arr[0]    # stores maximum sub of subarray found

        for i in range(1,n):
            cur = arr[i]    # current element
            sub_sum = max(cur, sub_sum+cur)     #T(O) = 0
            max_sum = max(max_sum, sub_sum)     # T(O) = 0

        return max_sum
    
if __name__=="__main__":
    obj = Solution()
    nums = list(map(int, input("Enter array of integers: ").split(",")))
    res = obj.kadaneAlgo(nums)
    print(res)

# T(O) = n